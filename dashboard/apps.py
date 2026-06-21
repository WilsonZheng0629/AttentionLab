import streamlit as st
import pandas as pd
import plotly.express as px


# Page Title
st.set_page_config(page_title="AttentionLab", layout="wide")

st.title("AttentionLab")
st.subheader("Creator Intelligence Dashboard")

# Load Data
df = pd.read_csv("data/cleaned_attentionlab_data.csv")
filtered_df = df.copy()


# KPI CALCULATIONS

total_views = df["views"].sum()

total_videos = len(df)
total_views = df["views"].sum()
avg_engagement = df["engagement_rate"].mean()
total_followers = df["followers_gained"].sum()

engagement_rate = (
    (
        df["likes"]
        + df["comments"]
        + df["shares"]
        + df["saves"]
    ).sum()
    / total_views
) * 100


# KPI CARDS

col1, col2, col3, col4 = st.columns(4)

col1.metric("Videos", total_videos)

col2.metric("Views", f"{total_views:,}")

col3.metric(
    "Avg Engagement",
    f"{avg_engagement:.2%}"
)

col4.metric(
    "Followers Gained",
    f"{total_followers:,}"
)

# Charts and Visualizations

# VIEWS BY TOPIC 
topic_views = (
    filtered_df.groupby("topic")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(topic_views)

# VIEWS BY PLATFORM
platform_views = (
    filtered_df.groupby("platform")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(platform_views)

# ENGAGEMENT RATE BY FORMAT  
format_engagement = (
    filtered_df.groupby("format")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(format_engagement)

# Side Bar Filters

platform_filter = st.sidebar.selectbox(
    "Platform",
    ["All"] + list(df["platform"].unique()),
    key="platform_filter"
)

topic_filter = st.sidebar.selectbox(
    "Topic",
    ["All"] + list(df["topic"].unique()),
    key="topic_filter"
)

format_filter = st.sidebar.selectbox(
    "Format",
    ["All"] + list(df["format"].unique()),
    key="format_filter"
)

# Apply Filters

if platform_filter != "All":
    filtered_df = filtered_df[
        filtered_df["platform"] == platform_filter
    ]

if topic_filter != "All":
    filtered_df = filtered_df[
        filtered_df["topic"] == topic_filter
    ]

if format_filter != "All":
    filtered_df = filtered_df[
        filtered_df["format"] == format_filter
    ]

# Topic Analysis Section
st.header("Topic Analysis")

# Average Views by Topic 
topic_views = (
    filtered_df
    .groupby("topic")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Views by Topic")

st.bar_chart(topic_views)

# and Engagement by Topic

topic_engagement = (
    filtered_df
    .groupby("topic")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Engagement by Topic")

st.bar_chart(topic_engagement)


# Format Analysis Section
st.header("Format Analysis")

# Views by Format

format_views = (
    filtered_df
    .groupby("format")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(format_views)

# Engagement by Format

format_engagement = (
    filtered_df
    .groupby("format")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(format_engagement)

# Hook Analysis Section
st.header("Hook Analysis")

hook_views = (
    filtered_df
    .groupby("hook_type")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(hook_views)

# Top Performing Video Types
st.header("Top Performing Videos")

top_videos = (
    filtered_df
    .sort_values(
        by="views",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_videos[
        [
            "caption",
            "platform",
            "topic",
            "format",
            "views",
            "engagement_rate"
        ]
    ]
)




# KEY INSIGHTS

st.header("Key Insights")

st.write("""
• AI content generated the highest average views.

• Tutorial videos had stronger engagement.

• Short-form content between 15–30 seconds performed best.

• TikTok generated the highest average reach.
""")

