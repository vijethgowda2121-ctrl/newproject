import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Geospatial Analysis",
    layout="wide"
)

st.title("🌍 Geospatial Analysis Dashboard")

# Sample GPS data
data = pd.DataFrame({
    "lat": [12.9716, 12.9352, 12.9279, 12.9141, 12.9980],
    "lon": [77.5946, 77.6245, 77.6271, 77.6387, 77.6100],
    "Vehicle": ["V1", "V2", "V3", "V4", "V5"],
    "Mileage": [18, 22, 20, 25, 19]
})

# Display data
st.subheader("Vehicle Location Data")
st.dataframe(data)

# Map visualization
st.subheader("Vehicle Locations")
st.map(data[["lat", "lon"]])

# Mileage analysis
st.subheader("Mileage Analysis")
st.bar_chart(data.set_index("Vehicle")["Mileage"])

# Statistics
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Vehicles", len(data))

with col2:
    st.metric("Average Mileage", round(data["Mileage"].mean(), 2))

with col3:
    st.metric("Maximum Mileage", data["Mileage"].max())
