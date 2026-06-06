import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Overview Dashboard",
    layout="wide"
)

st.title("📊 Overview Dashboard")

# Sample data
sessions = pd.DataFrame({
    "Date": ["2025-01-01", "2025-01-02", "2025-01-03", "2025-01-04"],
    "Sessions": [120, 150, 180, 140]
})

nodes = pd.DataFrame({
    "Node": ["Node A", "Node B", "Node C"],
    "Users": [45, 60, 35]
})

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sessions", int(sessions["Sessions"].sum()))

with col2:
    st.metric("Average Sessions", round(sessions["Sessions"].mean(), 2))

with col3:
    st.metric("Total Nodes", len(nodes))

# Session trend
st.subheader("Session Trend")
st.line_chart(sessions.set_index("Date")["Sessions"])

# Node usage
st.subheader("Node Usage")
st.bar_chart(nodes.set_index("Node")["Users"])

# Data tables
st.subheader("Session Data")
st.dataframe(sessions)

st.subheader("Node Data")
st.dataframe(nodes)

st.success("Overview dashboard loaded successfully.")
