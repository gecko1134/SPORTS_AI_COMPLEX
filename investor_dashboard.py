import streamlit as st
import pandas as pd

st.set_page_config(page_title="Investor Dashboard", layout="wide")
st.title("💼 SPORTAI Investor Dashboard")

uploaded = st.file_uploader("📤 Upload your investor CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.success(f"Loaded {len(df)} records")

    st.sidebar.header("Filters")
    status = st.sidebar.selectbox("Status", options=["All"] + sorted(df["Status"].dropna().unique().tolist()))
    tier = st.sidebar.multiselect("Benefit Tier", options=df["Benefit Tier"].dropna().unique())

    filtered = df.copy()
    if status != "All":
        filtered = filtered[filtered["Status"] == status]
    if tier:
        filtered = filtered[filtered["Benefit Tier"].isin(tier)]

    st.dataframe(filtered)

    st.subheader("📈 Investment Summary")
    st.metric("Total Active Investors", len(df[df["Status"] == "Active"]))
    st.metric("Total Raised ($)", f"${df['Amount ($)'].sum():,.0f}")
else:
    st.info("Please upload an investor tracking CSV to begin.")