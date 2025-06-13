import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
from pathlib import Path

# ───────── Page config & green theme CSS ─────────
st.set_page_config(
    page_title="ClimaCrop Health",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    :root {
        --primary-color: #2E7D32;
        --background-color: #F1F8E9;
        --secondary-bg-color: #A5D6A7;
        --text-color: #1B5E20;
        --insight-bg: #1B5E20;
    }
    .stApp { background-color: var(--background-color); }
    h1, h2, h3, h4, .css-1d391kg { color: var(--primary-color) !important; }
    .css-1d391kg, .css-18e3th9 { background-color: var(--secondary-bg-color) !important; }

/* agricultural: pale yellow-green body, mustard border, dark green text */
.insight-box-ag {
  background-color: #F7FCB9;       /* pale yellow-green */
  border-left: 4px solid #FFBF00;  /* mustard */
  padding: 16px;
  margin: 24px 0;
  color: var(--primary-color);     /* same as your “Best Model…” headings */
  font-size: 0.95rem;
  line-height: 1.4;
}

/* wild: pale green body, dark green border, dark green text */
.insight-box-wd {
  background-color: #E7F4E9;          /* pale green */
  border-left: 4px solid var(--primary-color);  /* dark green */
  padding: 16px;
  margin: 24px 0;
  color: var(--primary-color);
  font-size: 0.95rem;
  line-height: 1.4;
}

/* insight boxes share the sidebar’s background */
.insight-box-ag,
.insight-box-wd {
    background-color: var(--secondary-bg-color);  /* same as sidebar */
    padding: 16px;
    margin: 24px 0;
    font-size: 0.95rem;
    line-height: 1.4;
    color: #1B5E20; /* dark-green text for max contrast */
}

/* accent stripe on the left */
.insight-box-ag {
    border-left: 4px solid #1F78B4;  /* ColorBrewer blue accent */
}
.insight-box-wd {
    border-left: 4px solid #2E7D32;  /* matching dark-green accent */
}

.insight-box-ag ul,
.insight-box-wd ul {
    margin: 0;
    padding-left: 1.2em;
}
.insight-box-ag li,
.insight-box-wd li {
    margin-bottom: 8px;
}

.insight-box-ag ul,
.insight-box-wd ul {
  margin: 0;
  padding-left: 1.2em;
}
.insight-box-ag li,
.insight-box-wd li {
  margin-bottom: 8px;
}
    </style>
    """,
    unsafe_allow_html=True
)

# ───────── locate the images folder ─────────
ROOT    = Path(__file__).parent.parent
IMG_DIR = ROOT / "images"

# ───────── embed sizing constants ─────────
EMBED_WIDTH  = 700
EMBED_HEIGHT = 500

# ───────── define hard-coded CV & Test data ─────────
cv_data_ag = {
    "Ridge-spline":  [0.56,  0.457, 0.55,  0.565, 0.519],
    "RandomForest":  [0.575, 0.512, 0.585, 0.593, 0.531],
    "XGB":           [0.596, 0.453, 0.573, 0.614, 0.558],
    "SVR":           [0.568, 0.443, 0.560, 0.541, 0.551],
    "Stacking":      [0.596, 0.479, 0.588, 0.620, 0.572],
}
cv_data_wd = {
    "Ridge-spline":  [0.497, 0.608, 0.627, 0.364, 0.601],
    "RandomForest":  [0.476, 0.520, 0.564, 0.313, 0.452],
    "XGB":           [0.417, 0.457, 0.495, 0.223, 0.274],
    "SVR":           [0.354, 0.532, 0.611, 0.351, 0.547],
    "Stacking":      [0.491, 0.588, 0.610, 0.368, 0.543],
}
test_scores = {
    "MSE": {
        "Agricultural Default Stacking": 0.02879,
        "Wild Tuned Ridge-spline":       0.03014,
    },
    "R²": {
        "Agricultural Default Stacking": 0.527,
        "Wild Tuned Ridge-spline":       0.516,
    },
}

# ───────── helper to load HTML and fix encoding ─────────
def load_and_fix(path: Path) -> str:
    txt = path.read_text(encoding="utf-8")
    return txt.replace("RÂ²", "R²").replace("$R^2$", "R²")

def insight_box(items: list[str], style: str = "ag"):
    """
    items: list of bullet-point strings
    style: "ag" for Agricultural (blue), "wd" for Wild (green)
    """
    cls = "insight-box-ag" if style == "ag" else "insight-box-wd"
    html = f"<div class='{cls}'><ul>\n"
    for it in items:
        html += f"  <li>{it}</li>\n"
    html += "</ul></div>"
    st.markdown(html, unsafe_allow_html=True)


# ───────── top-level tabs ─────────
tab1, tab2, tab3 = st.tabs([
    "Predicted vs Actual",
    "Model Rankings",
    "Feature Importances"
])

# ───────── Tab 1: Predicted vs Actual ─────────
with tab1:
    ag_t, wd_t = st.tabs(["🌾 Agricultural", "🌲 Wild"])

    # ───────── Agricultural Block ─────────
    with ag_t:
        st.header("Agricultural Systems")

        # (1) Per-model CV R² scatter
        st.subheader("Per-Model CV R² Scatter Plots")
        models = ["Ridge", "RandomForest", "XGB", "SVR", "Stacking"]
        choice_ag = st.selectbox("Choose Agricultural model", models, key="r2_ag")
        html_r2_ag = IMG_DIR / f"r2_Agricultural_{choice_ag}.html"
        if html_r2_ag.exists():
            components.html(
                load_and_fix(html_r2_ag),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.warning(f"Drop `{html_r2_ag.name}` into `{IMG_DIR.name}/`")

        st.markdown("---")

        # (2) Best-model: Actual vs Predicted (Train)
        st.subheader("Best Model: Actual vs Predicted (Train)")
        file_train_ag = IMG_DIR / "actual_vs_Agricultural_train.html"
        if file_train_ag.exists():
            components.html(
                load_and_fix(file_train_ag),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.info(f"Drop `{file_train_ag.name}` into `{IMG_DIR.name}/`")

        # (3) Best-model: Actual vs Predicted (Test)
        st.subheader("Best Model: Actual vs Predicted (Test)")
        file_test_ag = IMG_DIR / "actual_vs_Agricultural_test.html"
        if file_test_ag.exists():
            components.html(
                load_and_fix(file_test_ag),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.info(f"Drop `{file_test_ag.name}` into `{IMG_DIR.name}/`")

        # Insight box (Agricultural)
        insight_box([
            "Points close to the diagonal indicate strong alignment between predicted and actual values.",
            "For farmers, this means you can trust the model to forecast disease pressure and optimize interventions.",
            "For environmental agencies, this validates the model’s reliability across diverse conditions."
        ], style="ag")
        
        insight_box([
        "Scatter R² values in Tab 1 measure fit on the entire train/test splits, which can be optimistic.",
        "The 5-Fold CV table (Tab 2) averages R² over held-out folds, giving a more conservative, unbiased estimate.",
        "Large differences highlight data variance and help detect potential overfitting."
    ], style="ag")


    # ───────── Wild Block ─────────
    with wd_t:
        st.header("Wild Systems")

        # (1) Per-model CV R² scatter
        st.subheader("Per-Model CV R² Scatter Plots")
        choice_wd = st.selectbox("Choose Wild model", models, key="r2_wd")
        html_r2_wd = IMG_DIR / f"r2_Wild_{choice_wd}.html"
        if html_r2_wd.exists():
            components.html(
                load_and_fix(html_r2_wd),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.warning(f"Drop `{html_r2_wd.name}` into `{IMG_DIR.name}/`")

        st.markdown("---")

        # (2) Best-model: Actual vs Predicted (Train)
        st.subheader("Best Model: Actual vs Predicted (Train)")
        file_train_wd = IMG_DIR / "actual_vs_Wild_train.html"
        if file_train_wd.exists():
            components.html(
                load_and_fix(file_train_wd),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.info(f"Drop `{file_train_wd.name}` into `{IMG_DIR.name}/`")

        # (3) Best-model: Actual vs Predicted (Test)
        st.subheader("Best Model: Actual vs Predicted (Test)")
        file_test_wd = IMG_DIR / "actual_vs_Wild_test.html"
        if file_test_wd.exists():
            components.html(
                load_and_fix(file_test_wd),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.info(f"Drop `{file_test_wd.name}` into `{IMG_DIR.name}/`")

        # Insight box (Wild)
        insight_box([
            "Shows how well the model tracks natural outbreak patterns in wild systems.",
            "Agencies can prioritize surveillance in areas with larger prediction errors.",
            "Supports early-warning efforts to protect ecosystem health."
        ], style="wd")
        
        insight_box([
        "Scatter R² values in Tab 1 measure fit on entire train/test splits and may appear higher.",
        "The 5-Fold CV table (Tab 2) reports average R² across validation folds, reflecting true generalization.",
        "Discrepancies between them reveal model stability and highlight overfitting risks."
    ], style="wd")


# ───────── Tab 2: Model Rankings ─────────
with tab2:
    st.subheader("Model Rankings: R² Summaries")
    ag_tab, wd_tab = st.tabs(["🌾 Agricultural", "🌲 Wild"])

    # prepare summaries
    def summarize(cv_dict):
        return (
            pd.DataFrame([
                {"Model": m, "Mean R²": arr.mean(), "Std R²": arr.std()}
                for m, arr in {k: np.array(v) for k, v in cv_dict.items()}.items()
            ])
            .sort_values("Mean R²", ascending=False)
            .reset_index(drop=True)
        )
    summary_ag = summarize(cv_data_ag)
    summary_wd = summarize(cv_data_wd)

    # ─── Agricultural Rankings ──────────────────────────────
    with ag_tab:
        st.markdown("**Train (5-Fold CV) R² Table**")
        st.table(summary_ag)

        st.markdown("**Train (5-Fold CV) R² Chart**")
        f_ag = IMG_DIR / "cv_summary_ag.html"
        if f_ag.exists():
            components.html(
                load_and_fix(f_ag),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.info(f"Drop `{f_ag.name}` into `{IMG_DIR.name}/`")


        # Insight box (Agricultural)
        insight_box([
            "The Stacking model has the highest mean R², meaning it explains the most variance in disease outcomes.",
            "Farmers can adopt this top model to get the most reliable predictions for outbreak timing.",
            "Environmental planners can focus resources on scenarios where model confidence is highest."
        ], style="ag")


    # ─── Wild Rankings ──────────────────────────────
    with wd_tab:
        st.markdown("**Train (5-Fold CV) R² Table**")
        st.table(summary_wd)

        st.markdown("**Train (5-Fold CV) R² Chart**")
        f_wd = IMG_DIR / "cv_summary_wd.html"
        if f_wd.exists():
            components.html(
                load_and_fix(f_wd),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.info(f"Drop `{f_wd.name}` into `{IMG_DIR.name}/`")


        # Insight box (Wild)
        insight_box([
            "The Ridge-spline model leads in wild settings, capturing key environmental variability.",
            "Agencies can use this to target monitoring in areas with the greatest predicted fluctuations.",
            "Supports ecosystem health efforts by highlighting where model accuracy is strongest."
        ], style="wd")

        
        
# ───────── Tab 3: Feature Importances ─────────
with tab3:
    st.subheader("Permutation Importances")
    ag_tab, wd_tab = st.tabs(["🌾 Agricultural", "🌲 Wild"])

    # ─── Agricultural Feature Importances ──────────────────────────────
    with ag_tab:
        f = IMG_DIR / "perm_importance_ag.html"
        if f.exists():
            components.html(
                load_and_fix(f),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.error(f"Missing `{f.name}`")

        # Insight box (Agricultural)
        insight_box([
            "Temperature and detection method are the strongest drivers of disease risk in crops.",
            "Farmers should closely monitor unusual temperature spikes to preempt outbreaks.",
            "Targeted interventions on key features can reduce pesticide use and improve yields."
        ], style="ag")

    # ─── Wild Feature Importances ──────────────────────────────
    with wd_tab:
        f = IMG_DIR / "perm_importance_wd.html"
        if f.exists():
            components.html(
                load_and_fix(f),
                height=EMBED_HEIGHT,
                width=EMBED_WIDTH,
                scrolling=True
            )
        else:
            st.error(f"Missing `{f.name}`")

        # Insight box (Wild)
        insight_box([
            "Contemporary temperature variability dominates wild-system disease predictions.",
            "Conservation teams can focus on areas with shifting climate patterns for early warning.",
            "Understanding key drivers helps allocate surveillance where it’s most needed."
        ], style="wd")
