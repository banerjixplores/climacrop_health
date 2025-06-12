# pages/04_Climate_Distributions.py

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.header("Climate Distributions by Pathogen Type & System")
st.markdown("Choose **Temperature** or **Rainfall** to view the violin plots.")

# ─── locate images folder ────────────────────────────────────────────────
ROOT    = Path(__file__).parent.parent
IMG_DIR = ROOT / "images"

# ─── map metric → HTML filename ───────────────────────────────────────────
violin_map = {
    "Temperature": "Violin_Temp_pathost.html",
    "Rainfall":    "Violin_Rain_pathost.html",
}

# ─── user selects metric ───────────────────────────────────────────────────
metric = st.selectbox("Climate Metric", list(violin_map.keys()))

# ─── embed the corresponding HTML ─────────────────────────────────────────
html_file = IMG_DIR / violin_map[metric]
if not html_file.exists():
    st.error(f"Missing `{html_file.name}` in `images/` folder.")
else:
    components.html(
        html_file.read_text(encoding="utf-8"),
        height=800,
        scrolling=True
    )
