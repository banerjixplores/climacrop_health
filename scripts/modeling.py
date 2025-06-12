# scripts/modeling.py

import pandas as pd
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.ensemble     import StackingRegressor
from sklearn.linear_model import RidgeCV
from sklearn.metrics      import r2_score, mean_squared_error

from pipelines import (
    make_spline_preprocessor,
    make_ridge_spline_pipeline,
    make_rf_pipeline,
    make_xgb_pipeline,
    make_svr_pipeline
)

RANDOM_STATE = 42
TEST_SIZE    = 0.2
CV_FOLDS     = 5

def load_data(path):
    """Load processed data (Parquet or CSV)."""
    if path.endswith(".parquet"):
        return pd.read_parquet(path)
    return pd.read_csv(path, index_col=0)

def split_subsets(df, target="incidence", system="system_type"):
    """Split into (X_ag, y_ag) and (X_wd, y_wd)."""
    X = df.drop(columns=[target])
    y = df[target]
    ag = df[system] == "Agricultural"
    wd = df[system] == "Wild"
    return X[ag], y[ag], X[wd], y[wd]

def make_splits(X_ag, y_ag, X_wd, y_wd):
    """80/20 train/test split for both subsets."""
    return train_test_split(
        X_ag, y_ag, X_wd, y_wd,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

def tune_agricultural(X_train, y_train, preprocessor):
    """GridSearchCV on Stacking (XGB + Ridge) for Agri."""
    # build pipelines
    pipe_xgb    = make_xgb_pipeline(preprocessor)
    pipe_r_spl  = make_ridge_spline_pipeline(preprocessor)
    stack_ag    = StackingRegressor(
        estimators=[("xgb", pipe_xgb), ("r_spl", pipe_r_spl)],
        final_estimator=RidgeCV(alphas=[0.1,1.0,10.0]),
        n_jobs=-1, passthrough=False
    )
    param_grid = {
        "xgb__regressor__learning_rate": [0.01, 0.1],
        "xgb__regressor__max_depth":      [3, 5],
        "r_spl__regressor__alphas":       [[0.001,0.01,0.1], [0.01,0.1,1.0]]
    }
    cv = KFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    gs = GridSearchCV(stack_ag, param_grid, cv=cv, scoring="r2", n_jobs=-1, verbose=0)
    gs.fit(X_train, y_train)
    return gs

def tune_wild(X_train, y_train, preprocessor):
    """GridSearchCV on Ridge-spline for Wild."""
    pipe_r_spl = make_ridge_spline_pipeline(preprocessor)
    param_grid = {
        "preprocessor__clim__spline__n_knots": [5,7,9],
        "preprocessor__clim__spline__degree":  [3,4],
        "regressor__alphas":                  [[0.001,0.01,0.1], [0.01,0.1,1.0], [0.1,1.0,10.0]]
    }
    cv = KFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_STATE)
    gs = GridSearchCV(pipe_r_spl, param_grid, cv=cv, scoring="r2", n_jobs=-1, verbose=0)
    gs.fit(X_train, y_train)
    return gs

def get_modeling_results(data_path):
    """Run full workflow, return test metrics & fitted GridSearchCV objects."""
    df       = load_data(data_path)
    X_ag, y_ag, X_wd, y_wd = split_subsets(df)
    X_at, X_ae, y_at, y_ae, X_wt, X_we, y_wt, y_we = make_splits(X_ag,y_ag,X_wd,y_wd)

    # define columns (match your notebook)
    climate_cols = ["monthly_temp", "monthly_precip", "contemp_temp", "contemp_precip"]
    other_numeric = [c for c in X_ag.columns if c not in climate_cols and X_ag[c].dtype in ("int64","float64")]
    categorical   = [c for c in X_ag.columns if X_ag[c].dtype == "object"]

    preproc = make_spline_preprocessor(climate_cols, other_numeric, categorical)

    grid_ag = tune_agricultural(X_at, y_at, preproc)
    grid_wd = tune_wild(X_wt, y_wt, preproc)

    # compute test‐set metrics
    def eval_best(gs, X_te, y_te):
        mdl = gs.best_estimator_
        ypr = mdl.predict(X_te)
        return {
            "R2":  r2_score(y_te, ypr),
            "MSE": mean_squared_error(y_te, ypr)
        }

    metrics = pd.DataFrame([
        {"subset": "Agricultural", **eval_best(grid_ag, X_ae, y_ae)},
        {"subset": "Wild",         **eval_best(grid_wd, X_we, y_we)}
    ])

    return {
        "metrics":   metrics,
        "grid_ag":   grid_ag,
        "grid_wd":   grid_wd,
        "X_ag_test": X_ae, "y_ag_test": y_ae,
        "X_wd_test": X_we, "y_wd_test": y_we
    }
