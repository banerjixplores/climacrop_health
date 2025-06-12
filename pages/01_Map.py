# pages/01_Map.py

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.header("Where Outbreaks Happen?")
st.markdown("Color = mean monthly temperature; Shape = Agricultural vs. Wild")

# locate the HTML file
ROOT    = Path(__file__).parent.parent
HTML    = ROOT / "images" / "global_map.html"

# read once
html_str = HTML.read_text(encoding="utf-8")

# embed without scrollbars, sized to container
components.html(
    html_str,
    height=700,     # bump this up as needed
    width=1200,     # optional — you can omit or adjust
    scrolling=False
)
