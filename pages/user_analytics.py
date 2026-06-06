import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="User Analytics",
    layout="wide"
)

st.title("👥 User Analytics Dashboard")

# Sample user data
users = pd.DataFrame({
    "User": ["User1", "User2", "User3", "User4", "User5"],
    "Sessions": [15, 22, 18, 30, 12],
    "Data_Usage_GB": [2.5, 4.1, 3.2, 5.0, 1.8]
})

# Display data
st.subheader("User Data")
st.dataframe(users)

# Sessions chart
st.subheader("Sessions per User")
st.bar_chart(users.set_index("User")["Sessions"])

# Data usage chart
st.subheader("Data Usage (GB)")
st.line_chart(users.set_index("User")["Data_Usage_GB"])

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Users", len(users))

with col2:
    st.metric("Total Sessions", int(users["Sessions"].sum()))

with col3:
    st.metric("Average Data Usage", round(users["Data_Usage_GB"].mean(), 2))

# Top user
top_user = users.loc[users["Sessions"].idxmax()]

st.success(
    f"Most active user: {top_user['User']} with "
    f"{top_user['Sessions']} sessions."
)
