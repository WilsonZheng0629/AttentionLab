import streamlit as st
import pandas as pd
import plotly.express as px

# Page Title
st.set_page_config(page_title="AttentionLab", layout="wide")

st.title("AttentionLab")
st.subheader("Creator Intelligence Dashboard")

# Load Data
df = pd.read_csv("data/videos.csv")

# KPI CALCULATIONS

total_views = df["Views"].sum()
total_videos = len(df)

engagement_rate = (
    (
        df["Likes"]
        + df["Comments"]
        + df["Shares"]
        + df["Saves"]
    ).sum()
    / total_views
) * 100


# KPI CARDS

col1, col2, col3 = st.columns(3)

col1.metric("Total Views", f"{total_views:,}")
col2.metric("Total Videos", total_videos)
col3.metric("Avg Engagement", f"{engagement_rate:.2f}%")

st.divider()


# VIEWS BY HOOK TYPE


hook_views = (
    df.groupby("Hook_Type")["Views"]
    .mean()
    .reset_index()
)

fig1 = px.bar(
    hook_views,
    x="Hook_Type",
    y="Views",
    title="Average Views by Hook Type"
)

st.plotly_chart(fig1, use_container_width=True)

# VIEWS BY CATEGORY

category_views = (
    df.groupby("Category")["Views"]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    category_views,
    x="Category",
    y="Views",
    title="Average Views by Category"
)

st.plotly_chart(fig2, use_container_width=True)
