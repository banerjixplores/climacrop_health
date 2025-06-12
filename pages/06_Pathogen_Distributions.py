# pages/05_Pathogen_Distributions.py

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.header("Pathogen & Host Distributions")
st.markdown("Stacked counts of agent & host orders by system.")

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
