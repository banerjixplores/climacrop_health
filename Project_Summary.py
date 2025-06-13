import streamlit as st
from pathlib import Path

# Build the correct path to your icon folder
ICON_PATH = Path(__file__).parent / "images" / "plant_health_logo.ico"

st.set_page_config(
    page_title="Plant Health Dashboard",
    page_icon=str(ICON_PATH),    # Streamlit will load the .ico for you
    layout="wide",
)

st.markdown(
    "<h1 style='color:#2E7D32; text-align:center;'>🍃 ClimaCrop Health: Plant Disease & Climate Impact Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown("""
**Project Summary**  
This dashboard brings together 4,339 plant‐disease surveys linked to climate data, allowing:
- **Where** outbreaks occur?  
- **How** anomalies drive disease? 
- **Which** climate metrics matter most? 
- **Who** (pathogen groups) are high‐risk ?
- **What** our models reveal? 

**Dataset:**  
[`merged_climate_disease_final.csv`](../data/processed/merged_climate_disease_final.csv)

_For full details, see the [GitHub README](https://github.com/banerjixplores/climacrop_health#readme)._
""")
