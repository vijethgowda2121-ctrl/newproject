import streamlit as st
import pandas as pd
import plotly.express as px

st.title("WiFi Session Analysis")

df = pd.read_csv("wifi_session.csv")

fig = px.histogram(
    df,
    x="session_duration",
    nbins=30,
    title="Session Duration Distribution"
)

st.plotly_chart(fig, use_container_width=True)
