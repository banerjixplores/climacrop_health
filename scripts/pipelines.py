# scripts/pipelines.py

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, SplineTransformer
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor

def make_preprocessor(numeric_cols, categorical_cols):
    """Basic impute+scale for numerics, impute+onehot for categoricals."""
    num_pipe = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale",  StandardScaler())
    ])
    cat_pipe = Pipeline([
        ("impute", SimpleImputer(strategy="constant", fill_value="Missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse=False))
    ])
    return ColumnTransformer([
        ("num", num_pipe, numeric_cols),
        ("cat", cat_pipe, categorical_cols)
    ], remainder="drop")

def make_spline_preprocessor(climate_cols, other_numeric_cols, categorical_cols,
                             n_knots=7, degree=3):
    """Spline‐transform climate features, scale others, and one‐hot cats."""
    clim_pipe = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("spline", SplineTransformer(n_knots=n_knots,
                                     degree=degree,
                                     include_bias=False)),
        ("scale",  StandardScaler())
    ])
    other_num_pipe = Pipeline([
        ("impute", SimpleImputer(strategy="median")),
        ("scale",  StandardScaler())
    ])
    cat_pipe = Pipeline([
        ("impute", SimpleImputer(strategy="constant", fill_value="Missing")),
        ("onehot", OneHotEncoder(handle_unknown="ignore", sparse=False))
    ])
    return ColumnTransformer([
        ("clim",     clim_pipe,    climate_cols),
        ("other_num",other_num_pipe,other_numeric_cols),
        ("cat",      cat_pipe,     categorical_cols),
    ], remainder="drop")

def make_ridge_spline_pipeline(preprocessor):
    """Pipeline: preprocessor → RidgeCV on splines."""
    return Pipeline([
        ("preprocessor", preprocessor),
        ("regressor",    RidgeCV(alphas=[0.1, 1.0, 10.0], store_cv_values=True))
    ])

def make_rf_pipeline(preprocessor):
    """Pipeline: preprocessor → RandomForest."""
    return Pipeline([
        ("preprocessor", preprocessor),
        ("regressor",    RandomForestRegressor(n_estimators=200, random_state=42))
    ])

def make_xgb_pipeline(preprocessor):
    """Pipeline: preprocessor → XGBoost."""
    return Pipeline([
        ("preprocessor", preprocessor),
        ("regressor",    XGBRegressor(n_estimators=100,
                                      learning_rate=0.1,
                                      random_state=42))
    ])

def make_svr_pipeline(preprocessor):
    """Pipeline: preprocessor → SVR."""
    return Pipeline([
        ("preprocessor", preprocessor),
        ("regressor",    SVR(C=1.0, epsilon=0.1))
    ])
