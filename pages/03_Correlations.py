from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# ───────── Page config & icon ─────────
ICON_PATH = Path(__file__).parent / "images" / "corr_icon.ico"
st.set_page_config(
    page_title="Correlations",
    page_icon="🌡",
    layout="wide",
)

# ───────── Custom CSS for callouts & expanders ─────────
st.markdown("""
<style>
/* green callout box */
.callout-note {
  background-color: #E8F5E9;
  border-left: 6px solid #2E7D32;
  padding: 16px;
  margin: 16px 0;
  color: #1B5E20;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
.callout-note strong {
  color: var(--primary-color);
}

/* expander header styling */
div[data-testid="stExpander"] > div[role="button"],
div[data-testid="stExpander"] button[role="button"] {
  background-color: #C7E9C0 !important;
  border-left: 4px solid #2E7D32 !important;
  border-radius: 4px !important;
  padding: 8px 16px !important;
  margin-bottom: 8px !important;
}
div[data-testid="stExpander"] svg {
  stroke: #2E7D32 !important;
}
</style>
""", unsafe_allow_html=True)

# ───────── Header & Intro ─────────
st.header("🌡 Climate Variable Correlations")
st.markdown("Which metrics move together—and which anomalies stand alone?")

# ───────── Goal note ─────────
st.markdown("""
<div class="callout-note">
  <strong>Goal:</strong> Show how different climate variables correlate with each other.  
  Dark blue indicates strong positive correlation, while dark red shows strong negative correlation.
</div>
""", unsafe_allow_html=True)

# ───────── Centered correlation heatmap ─────────
col1, col2, col3 = st.columns([1,2,1])
with col2:
    HTML = Path(__file__).parent.parent / "images" / "corr.html"
    components.html(HTML.read_text(encoding="utf-8"), height=700, width=700, scrolling=True)

# ───────── Centered caption ─────────
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
    <p style="
        text-align: center;
        color: var(--text-color);
        font-style: italic;
        margin-top: -8px;
    ">
        Correlation matrix: blue = positive, red = negative
    </p>
    """, unsafe_allow_html=True)

# ───────── Stakeholder Insights ─────────
st.markdown("#### Stakeholder Insights")
st.markdown("""
- **Technical Team:** Temperature metrics collapse into two clusters (historical vs. contemporary); anomalies are orthogonal—use them for feature selection.  
- **Farmer:** You only need to watch one rainfall measure (e.g. monthly) instead of juggling annual, monthly, and contemporary—simplify your weather alerts.  
- **Environmental Agency:** Focus on anomaly indices for early warning; reduce redundant sensor deployments for historical baselines.
""")
