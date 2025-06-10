import streamlit as st

st.set_page_config(
    page_title="Plant Disease Dashboard",
    page_icon="../plant_disease_risk_app/assets/plant_health_logo.jpg",
    layout="wide"
)

# Centered logo
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("../plant_disease_risk_app/assets/plant_health_logo.jpg", width=120)
st.markdown("</div>", unsafe_allow_html=True)

# Title & Navigation
st.title("Climate-Driven Plant Disease Risk Platform")

st.markdown("""
Welcome! Use the sidebar to navigate:

1. Exploratory Data Analysis
2. Hypotheses & Validation
3. Model Comparison
4. Scenario Simulator
5. About & Sources
""", unsafe_allow_html=True)

st.markdown("---")