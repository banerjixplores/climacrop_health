# pages/05_Pathogen_Distributions.py

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Pathogen & Host Diversity",
    page_icon="🦠",       # Only the first emoji will show as favicon
    layout="wide"
)

# ───────── Custom CSS for green callout ─────────
st.markdown("""
<style>
.callout-note {
  background-color: #E8F5E9;
  border-left: 6px solid #2E7D32;
  padding: 16px;
  margin: 28px 0 18px 0;
  color: #1B5E20;
  border-radius: 5px;
  box-shadow: 0 8px 32px rgba(44,62,80,0.16), 0 2px 12px rgba(44,62,80,0.11);
  font-size: 1.09rem;
}
.fig-caption {
  color: #388e3c;
  font-size: 0.96rem;
  text-align: center;
  margin-top: -18px;
  margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# ───────── Title ─────────

st.markdown(
    "<h1 style='text-align:center; color:#2E7D32;'>Pathogen & Host Diversity Across Agricultural and Natural Systems</h1>",
    unsafe_allow_html=True
)
st.markdown("""
<div class="callout-note">
  <strong>Goal:</strong> Explore which pathogens and plant host groups are most common in agricultural vs. natural systems—and how their diversity shifts across environments.
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
    st.markdown(
        "<div class='fig-caption'>"
        "<b>Figure:</b> Pathogen and host order counts by system. Each bar shows the number of disease surveys for each pathogen and host group in agricultural and natural plant systems."
        "</div>", unsafe_allow_html=True)
else:
    st.error(f"Missing `{overall_html.name}` in `/images` folder.")

# ───────── Stakeholder insights for overall plot ─────────
st.markdown("""
<div class="callout-note">
  <strong>Stakeholder Insights</strong>
  <ul>
    <li><b>Technical Team:</b> Viruses and eukaryotic parasites dominate agricultural surveys; bacterial and pest data are sparse—watch for imbalance in your modeling samples.</li>
    <li><b>Farmer:</b> Over 80% of crop disease surveys target viruses and fungal/eukaryotic parasites—focus your diagnostics accordingly.</li>
    <li><b>Environmental Agency:</b> Natural-plant surveys include more conifer ("Pinales") and grapevine ("Vitales") hosts—tailor wild-plant protection to these orders.</li>
  </ul>
</div>
""", unsafe_allow_html=True)

# ───────── breakdown by climate metric ─────────
st.subheader("Breakdown by Climate Metric")
st.markdown("Choose to view distributions by <b>Temperature</b> or <b>Rainfall</b>—see how different climate conditions shape pathogen and host group presence.", unsafe_allow_html=True)

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
    # Optional: add an accessibility-friendly caption
    st.markdown(
        f"<div class='fig-caption'><b>Figure:</b> Pathogen and host order counts distributed by {choice.replace('Distributions','').strip()} metric across systems.</div>",
        unsafe_allow_html=True
    )
else:
    st.error(f"Missing `{detail_html.name}` in `/images` folder.")

# ───────── Stakeholder insights for breakdown plot ─────────
st.markdown("""
<div class="callout-note">
  <strong>Explore how counts of pathogens and hosts are distributed across different temperature and rainfall conditions.</strong>
  <ul>
    <li><b>Technical Team:</b> Horizontal orientation makes heavy-tailed distributions (e.g., anomalies) easy to scan for outliers; interactive dropdown helps you spot skew and gaps by metric.</li>
    <li><b>Farmer:</b> Use “Temperature anomaly” to see how often your area exceeds +2 °C—plan for added irrigation or shading if those bins are crowded.</li>
    <li><b>Environmental Agency:</b> Compare “Rainfall anomaly” and “Contemporary precipitation” counts to prioritize weather station upgrades and disease early-warning efforts.</li>
  </ul>
</div>
""", unsafe_allow_html=True)
