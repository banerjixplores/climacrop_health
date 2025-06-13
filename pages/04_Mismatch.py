from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# ───────── Page config & icon ─────────
st.set_page_config(
    page_title="Weather Mismatch Effect",
    page_icon="🌡️",
    layout="wide",
)

st.markdown(
    "<h1 style='text-align:center; color:#2E7D32;'> When Weather Goes Off-Script: Disease Spikes in Crops and Natural Plants </h1>",
    unsafe_allow_html=True
)

# ───────── Custom CSS ─────────
st.markdown("""
<style>
.callout-note {
  background-color: #E8F5E9;
  border-left: 6px solid #2E7D32;
  padding: 16px;
  margin: 20px 0 10px 0;
  color: #1B5E20;
  border-radius: 5px;
  box-shadow: 0 4px 14px rgba(0,0,0,0.12);
  font-size: 1.07rem;
}
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

# ───────── Title & Intro ─────────
st.markdown("Explore how deviations from typical weather patterns—called anomalies—drive plant disease risk in wild and agricultural systems.")


# ───────── What is an “Anomaly”? ─────────
st.markdown("""
<div class="callout-note">
  <strong>What’s an anomaly?</strong>  
  An <b>anomaly</b> is simply how much this month's weather differs from the usual, long-term average for that place and season.<br>
  <i>Example:</i> If your region’s June average temperature is 20 °C, but this June was 23 °C, the temperature anomaly is <b>+3 °C</b>. Negative means cooler/drier, positive means warmer/wetter than usual.
</div>
""", unsafe_allow_html=True)

# ───────── How anomalies are computed (expander) ─────────
with st.expander("How are anomalies computed from the raw data? (see steps)"):
    st.markdown("""
**Temperature:**
- Survey (contemporary) temp is recorded in Kelvin—convert to °C:  
  `contemp_temp_C = contemp_temp - 273.15`
- Long-term monthly & annual means are in tenths of °C (WorldClim)—convert:  
  `monthly_temp_C = monthly_temp / 10`  
  `annual_mean_temp_C = annual_mean_temp / 10`
- **Temperature anomaly:**  
  `temp_anomaly_C = contemp_temp_C - monthly_temp_C`

**Rainfall:**
- Survey rainfall is already in mm/day.
- Monthly & annual means are in mm/month—convert to mm/day:  
  `monthly_precip_mm_per_day = monthly_precip / 30`  
  `annual_precip_mm_per_day = annual_precip / 30`
- **Rainfall anomaly:**  
  `rain_anomaly_daily = contemp_precip - monthly_precip_mm_per_day`
""")

# ───────── File paths ─────────
ROOT    = Path(__file__).parent.parent
IMG_DIR = ROOT / "images"
file_map = {
    ("Agricultural", "Temperature vs. Incidence"): "Ag_tempinc.html",
    ("Agricultural", "Rainfall vs. Incidence"):    "Ag_raininc.html",
    ("Wild",         "Temperature vs. Incidence"): "Wd_tempinc.html",
    ("Wild",         "Rainfall vs. Incidence"):    "Wd_raininc.html",
}

# ───────── User selections ─────────
system = st.selectbox("System", ["Agricultural", "Natural"])
metric = st.selectbox("Metric", ["Temperature vs. Incidence", "Rainfall vs. Incidence"])

chosen_file = file_map[(system, metric)]
html_path   = IMG_DIR / chosen_file

if not html_path.exists():
    st.error(f"Missing `{chosen_file}` in `/images` folder.")
else:
    components.html(
        html_path.read_text(encoding="utf-8"),
        height=600,
        scrolling=True
    )

# ───────── Stakeholder Insights ─────────
st.markdown("#### Stakeholder Insights")
if metric == "Temperature vs. Incidence":
    st.markdown("""
- **Technical Team:** Wild systems show a U-shaped response (“mismatch effect”) confirming strong anomaly × historical interaction. Agricultural systems remain nearly linear—buffered by management.
- **Farmer:** When your field’s temperature strays ±2 °C from normal, watch for spikes in wild-plant disease—but crops are safer until extremes.
- **Environmental Agency:** Set anomaly thresholds to trigger early alerts for outbreaks in protected wild areas.
""")
else:
    st.markdown("""
- **Technical Team:** Rain anomalies are largely independent of historical normals—making them prime predictors for disease mismatch models.
- **Farmer:** Just track a single rainfall anomaly (monthly), rather than many redundant metrics—simplifies your weather alerts.
- **Environmental Agency:** Use rainfall-anomaly alerts to focus monitoring and reduce redundant sensor deployments.
""")
