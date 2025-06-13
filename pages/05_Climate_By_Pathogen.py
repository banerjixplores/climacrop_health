from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# ───────── Page config & icon ─────────
st.set_page_config(
    page_title="Who Lives in What Climate?",
    page_icon="🌦️",
    layout="wide",
)

# ───────── Custom CSS for green callout ─────────
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
</style>
""", unsafe_allow_html=True)

# ───────── Title & Goal ─────────
st.markdown(
    "<h1 style='text-align:center; color:#2E7D32;'> Who Lives in What Climate? (By Pathogen & System) </h1>",
    unsafe_allow_html=True
)
st.markdown(
    '<div class="callout-note">'
    '<strong>Goal:</strong> To Compare the climate niches occupied by each pathogen group in Agricultural vs. Natural plant systems.<br>'
    'Violin plots show the temperature or rainfall “envelopes” for each group.'
    '</div>',
    unsafe_allow_html=True
)

# ─── locate images folder ─────────────────────────────
ROOT    = Path(__file__).parent.parent
IMG_DIR = ROOT / "images"

# ─── map metric → HTML filename ──────────────────────
violin_map = {
    "Temperature": "Violin_Temp_pathost.html",
    "Rainfall":    "Violin_Rain_pathost.html",
}

# ─── user selects metric ──────────────────────────────
metric = st.selectbox("Climate Metric", list(violin_map.keys()))

# ─── embed the corresponding HTML ────────────────────
html_file = IMG_DIR / violin_map[metric]
if not html_file.exists():
    st.error(f"Missing `{html_file.name}` in `images/` folder.")
else:
    components.html(
        html_file.read_text(encoding="utf-8"),
        height=500,
        scrolling=True
    )

st.markdown("""
<div class="callout-note">
  <strong>Interpretation:</strong> Pathogen groups have distinct climate preferences. 
  These plots help you see which groups are likely to thrive under different temperature or rainfall conditions.
</div>
""", unsafe_allow_html=True)


# ───────── Stakeholder Insights ─────────
st.markdown("#### Stakeholder Insights")
st.markdown("""
- **Technical Team:** Violin shapes show that pests occupy cooler/wetter niches in natural systems, while viruses span warmer/drier extremes in crops—consider grouping model residuals by pathogen type.
- **Farmer:** If you grow legumes (Fabales) at ~20–25 °C, expect more virus incidence; use this info to guide your planting schedule.
- **Environmental Agency:** Natural-system pathogens see rainfall anomalies up to –4 mm/day; prioritize surveillance in regions forecast for extreme drought.
""")
