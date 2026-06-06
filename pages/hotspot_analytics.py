import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Hotspot Analytics", layout="wide")

st.title("🔥 Hotspot Analytics Dashboard")

# Sample hotspot data
data = pd.DataFrame({
    "Hotspot": ["Area A", "Area B", "Area C", "Area D", "Area E"],
    "Events": [120, 85, 150, 95, 110],
    "Risk Score": [8.5, 6.2, 9.1, 7.0, 8.0]
})

# Display data
st.subheader("Hotspot Data")
st.dataframe(data)

# Event counts
st.subheader("Events by Hotspot")
st.bar_chart(data.set_index("Hotspot")["Events"])

# Risk scores
st.subheader("Risk Scores")
st.line_chart(data.set_index("Hotspot")["Risk Score"])

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Hotspots", len(data))

with col2:
    st.metric("Total Events", int(data["Events"].sum()))

with col3:
    st.metric("Average Risk", round(data["Risk Score"].mean(), 2))

# Top hotspot
top_hotspot = data.loc[data["Events"].idxmax()]

st.subheader("Top Hotspot")
st.success(
    f"{top_hotspot['Hotspot']} recorded the highest activity with "
    f"{top_hotspot['Events']} events."
)
