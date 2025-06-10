import streamlit as st

st.set_page_config(page_title="About & Sources", layout="wide")
st.title("ℹ️ About & Data Sources")

st.markdown("**Data Source:** Kirk et al. Dryad repository via `merged_climate_disease_final.csv`.")

st.markdown("**GitHub:** [ClimaCrop Health](https://github.com/banerjixplores/climacrop_health)")

st.markdown("**Modeling:** Ridge, RF, XGBoost, SVR, Stacking algorithms.")

st.markdown("**Limitations & Next Steps:**")
st.write("- Varies by region & host.")
st.write("- Add abiotic/biotic factors.")
st.write("- Batch scenario simulation.")