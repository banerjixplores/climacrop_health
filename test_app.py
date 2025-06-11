import streamlit as st

st.set_page_config(page_title="Test Dashboard", layout="wide")
st.title("🌱 Test Plant Health Dashboard")

st.markdown("""
This is a simple test to confirm Streamlit is working correctly.
""")

temp = st.slider("Temperature Anomaly (°C)", -5.0, 5.0, 0.0)
rain = st.slider("Rainfall Anomaly (mm)", -100.0, 100.0, 0.0)

if st.button("Predict"):
    st.success(f"Simulated prediction: Temp = {temp}, Rain = {rain}")