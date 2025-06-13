# pages/05_Pathogen_Distributions.py

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

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

st.markdown(
    "<h1 style='text-align:center; color:#2E7D32;'> Pathogen & Host Diversity Across Agricultural and Natural Systems </h1>",
    unsafe_allow_html=True
)
st.markdown("""
<div class="callout-note">
  <strong>Goal:</strong> Visualize the diversity and abundance of pathogen types and host orders in agricultural versus natural plant systems.  
</div>
""", unsafe_allow_html=True)

# ───────── locate the images folder ─────────
ROOT    = Path(__file__).parent.parent
IMG_DIR = ROOT / "images"

# ───────── embed the overall distribution ─────────
overall_html = IMG_DIR / "Pathogen_host_dist.html"
if overall_html.exists():
    components.html(
        overall_html.read_text(encoding="utf-8"),
        height=600,
        scrolling=True
    )
else:
    st.error(f"Missing `{overall_html.name}` in `/images` folder.")
    
st.markdown("""
<div class="callout-note">
  <strong>Stakeholder Insights</strong>
  <br>
  <ul>
    <li><b>Technical Team:</b> Viruses and eukaryotic parasites dominate agricultural surveys; bacterial and pest data are sparse—watch for imbalance in your modeling samples.</li>
    <li><b>Farmer:</b> Over 80% of crop disease surveys target viruses and fungal/eukaryotic parasites—focus your diagnostics accordingly.</li>
    <li><b>Environmental Agency:</b> Natural-plant surveys include more conifer ("Pinales") and grapevine ("Vitales") hosts—tailor wild-plant protection to these orders.</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# ───────── breakdown by climate metric ─────────
st.subheader("Breakdown by Climate Metric")
st.markdown("Select Temperature or Rainfall to see pathogen & host counts under each.")

dist_map = {
    "Temperature Distributions": "temp_pathogen_distributions.html",
    "Rainfall Distributions":    "precip_pathogen_distributions.html",
}

choice = st.selectbox("Distribution Type", list(dist_map.keys()))

detail_html = IMG_DIR / dist_map[choice]
if detail_html.exists():
    components.html(
        detail_html.read_text(encoding="utf-8"),
        height=600,
        scrolling=True
    )
else:
    st.error(f"Missing `{detail_html.name}` in `/images` folder.")

st.markdown("""
<div class="callout-note">
Explore how counts of pathogens and hosts are distributed across different temperature and rainfall conditions.

<br>
 <strong>Stakeholder Insights</strong>
 <br>
<ul>
  <li><b>Technical Team:</b> Horizontal orientation makes heavy-tailed distributions (e.g., anomalies) easy to scan for outliers; interactive dropdown helps you spot skew and gaps by metric.</li>
  <li><b>Farmer:</b> Use “Temperature anomaly” to see how often your area exceeds +2 °C—plan for added irrigation or shading if those bins are crowded.</li>
  <li><b>Environmental Agency:</b> Compare “Rainfall anomaly” and “Contemporary precipitation” counts to prioritize weather station upgrades and disease early-warning efforts.</li>
</ul>
</div>
""", unsafe_allow_html=True)

