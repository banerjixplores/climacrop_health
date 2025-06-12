from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.header("Model Insights: Feature Importances")
st.markdown("Top predictors from our ML pipeline.")

with open("images/feature_importance.html", "r") as f:
    components.html(f.read(), height=400, scrolling=True)
