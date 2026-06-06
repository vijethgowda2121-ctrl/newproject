import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Hotspot Analytics")

data = pd.DataFrame({
    "Location": ["A", "B", "C", "D"],
    "Visits": [120, 90, 150, 80]
})

fig = px.bar(
    data,
    x="Location",
    y="Visits",
    title="Hotspot Visits"
)

st.plotly_chart(fig, use_container_width=True)
