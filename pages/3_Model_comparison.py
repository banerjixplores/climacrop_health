import streamlit as st
import pandas as pd
import plotly.express as px
from mlModelCompare import compare_models

st.set_page_config(page_title="Model Comparison", layout="wide")
st.title("Model Comparison")

system = st.sidebar.selectbox("System Type", ["Agricultural", "Wild"])
metrics_df = compare_models(system=system)

st.dataframe(metrics_df)
st.subheader("Cross-Validated R² by Model")
fig_r2 = px.bar(metrics_df, x='Model', y='CV_R2', title=f"CV R² for {system} System")
st.plotly_chart(fig_r2, use_container_width=True)

st.subheader("Zone-wise Accuracy by Model")
acc_df = metrics_df.melt(id_vars='Model', value_vars=['Zone_Acc_Low','Zone_Acc_Med','Zone_Acc_High'], var_name='Zone', value_name='Accuracy')
fig_acc = px.bar(acc_df, x='Model', y='Accuracy', color='Zone', title=f"Zone-wise Accuracy for {system} System")
st.plotly_chart(fig_acc, use_container_width=True)