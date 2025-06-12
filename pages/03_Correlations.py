from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.header("Climate Variable Correlations")
st.markdown("Which metrics move together—and which anomalies stand alone?")

ROOT = Path(__file__).parent.parent
HTML = ROOT / "images" / "corr.html"

components.html( HTML.read_text(), height=700, scrolling=True )

