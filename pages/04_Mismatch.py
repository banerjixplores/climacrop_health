# pages/03_Mismatch.py

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.header("Mismatch Effect: Temperature & Rainfall vs. Incidence")
st.markdown(
    "Select a system and metric to explore how anomalies drive disease incidence."
)

# ─────────── Paths ───────────
ROOT    = Path(__file__).parent.parent
IMG_DIR = ROOT / "images"

# ─────────── File lookup ───────────
file_map = {
    ("Agricultural", "Temperature vs. Incidence"): "Ag_tempinc.html",
    ("Agricultural", "Rainfall vs. Incidence"):   "Ag_raininc.html",
    ("Wild",          "Temperature vs. Incidence"): "Wd_tempinc.html",
    ("Wild",          "Rainfall vs. Incidence"):   "Wd_raininc.html",
}

# ─────────── User selection ───────────
system = st.selectbox("System", ["Agricultural", "Wild"])
metric = st.selectbox("Metric", ["Temperature vs. Incidence", "Rainfall vs. Incidence"])

# ─────────── Embed HTML ───────────
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
