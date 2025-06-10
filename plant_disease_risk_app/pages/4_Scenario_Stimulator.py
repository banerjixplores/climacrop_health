import streamlit as st
import joblib

st.set_page_config(page_title="Scenario Simulator", layout="wide")
st.title("Scenario Simulator")

temp = st.sidebar.slider("Temperature Anomaly (°C)", -5.0, 5.0, 0.0, 0.1)
rain = st.sidebar.slider("Rainfall Anomaly (mm)", -200.0, 200.0, 0.0, 10.0)

model = joblib.load("models/best_model.joblib")
zone_pred = model.predict([[temp, rain]])[0]

st.subheader("Predicted Disease Incidence Zone")
st.write(f"**{zone_pred}**")

st.markdown("---")
st.subheader("Top Contributing Features (Placeholder)")
st.write("Replace with SHAP or coefficient contributions.")