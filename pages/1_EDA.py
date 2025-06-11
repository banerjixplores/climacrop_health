import streamlit as st
import pandas as pd
import plotly.express as px
from utils.colors import WILD_COLOR, AG_COLOR

st.set_page_config(page_title="EDA & Map", layout="wide")
st.title("Exploratory Data Analysis")

@st.cache_data
def load_data():
    return pd.read_csv("../plant_disease_risk_app/data/merged_climate_disease_final.csv")

df = load_data()

# Sidebar filter
system_type = st.sidebar.selectbox("System Type", ["All", "Wild", "Agricultural"])
if system_type != "All":
    df = df[df["Host_type"].str.lower() == system_type.lower()]

# Geographic map
st.subheader("Geographic Distribution of Disease Incidence")
fig_map = px.scatter_geo(
    df,
    lat='Latitude', lon='Longitude',
    color='incidence_zone',
    hover_name='location',
    hover_data=['Host_type', 'temp_anomaly', 'rain_anomaly'],
    projection='natural earth',
    title='Disease Incidence Zones by Location',
    color_discrete_map={
        'Low': WILD_COLOR,
        'Medium': AG_COLOR,
        'High': 'orange'
    }
)
st.plotly_chart(fig_map, use_container_width=True)

st.markdown("---")

# Average anomaly trends
st.subheader("Average Climate Anomalies by Zone")
trend_df = (
    df.groupby('incidence_zone')
      [['temp_anomaly','rain_anomaly']]
      .mean()
      .reset_index()
      .melt(id_vars='incidence_zone', var_name='Anomaly', value_name='Mean')
)
fig_line = px.line(
    trend_df, x='incidence_zone', y='Mean', color='Anomaly',
    title='Temp vs Rainfall Anomalies by Zone'
)
st.plotly_chart(fig_line, use_container_width=True)