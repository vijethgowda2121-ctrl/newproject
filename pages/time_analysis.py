import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Time Analysis",
    layout="wide"
)

st.title("⏱️ Time Analysis Dashboard")

# Sample hourly data
data = pd.DataFrame({
    "Hour": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00"],
    "Sessions": [25, 18, 65, 120, 95, 50]
})

# Display data
st.subheader("Hourly Activity Data")
st.dataframe(data)

# Activity trend
st.subheader("Activity Trend")
st.line_chart(data.set_index("Hour")["Sessions"])

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sessions", int(data["Sessions"].sum()))

with col2:
    st.metric("Peak Sessions", int(data["Sessions"].max()))

with col3:
    st.metric("Average Sessions", round(data["Sessions"].mean(), 2))

# Peak hour
peak = data.loc[data["Sessions"].idxmax()]

st.subheader("Peak Usage Time")
st.success(
    f"Highest activity occurred at {peak['Hour']} with "
    f"{peak['Sessions']} sessions."
)
