import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="AttentionLab", layout="wide")

# Load data
df = pd.read_csv("data/cleaned_attentionlab_data.csv")

# Title
st.title("AttentionLab")
st.subheader("Creator Intelligence Dashboard")

st.write("""
AttentionLab analyzes short-form content performance across platforms,
topics, formats, hooks, posting patterns, and production ROI.
""")

st.divider()

# Sidebar filters
st.sidebar.header("Filters")

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

# Apply filters
filtered_df = df.copy()

if platform_filter != "All":
    filtered_df = filtered_df[filtered_df["platform"] == platform_filter]

if topic_filter != "All":
    filtered_df = filtered_df[filtered_df["topic"] == topic_filter]

if format_filter != "All":
    filtered_df = filtered_df[filtered_df["format"] == format_filter]

# Executive Summary
st.header("Executive Summary")

total_videos = len(filtered_df)
total_views = filtered_df["views"].sum()
avg_engagement = filtered_df["engagement_rate"].mean()
total_followers = filtered_df["followers_gained"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Videos", total_videos)
col2.metric("Views", f"{total_views:,}")
col3.metric("Avg Engagement", f"{avg_engagement:.2%}")
col4.metric("Followers Gained", f"{total_followers:,}")

st.divider()

# Topic Analysis
st.header("Topic Analysis")

topic_views = (
    filtered_df.groupby("topic")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Views by Topic")
st.bar_chart(topic_views)
st.caption("Shows which content topics generate the highest average reach.")

topic_engagement = (
    filtered_df.groupby("topic")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Engagement by Topic")
st.bar_chart(topic_engagement)
st.caption("Shows which topics generate the strongest engagement rate.")

st.divider()

# Format Analysis
st.header("Format Analysis")

format_views = (
    filtered_df.groupby("format")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Views by Format")
st.bar_chart(format_views)
st.caption("Compares how different content formats perform by average views.")

format_engagement = (
    filtered_df.groupby("format")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Engagement by Format")
st.bar_chart(format_engagement)
st.caption("Compares how different formats perform by engagement rate.")

st.divider()

# Hook Analysis
st.header("Hook Analysis")

hook_views = (
    filtered_df.groupby("hook_type")["views"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average Views by Hook Type")
st.bar_chart(hook_views)
st.caption("Shows which opening hook styles generate the most average views.")

st.divider()

# Posting Pattern Analysis
st.header("Posting Pattern Analysis")

day_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

day_views = (
    filtered_df.groupby("day_of_week")["views"]
    .mean()
    .reindex(day_order)
)

st.subheader("Average Views by Day of Week")
st.bar_chart(day_views)
st.caption("Shows whether posting day is associated with stronger reach.")

weekend_views = (
    filtered_df.groupby("is_weekend")["views"]
    .mean()
)

st.subheader("Average Views: Weekday vs Weekend")
st.bar_chart(weekend_views)
st.caption("Compares average performance between weekday and weekend posts.")

st.divider()

# Video Length Analysis
st.header("Video Length Analysis")

length_views = (
    filtered_df.groupby("length_bucket")["views"]
    .mean()
)

st.subheader("Average Views by Video Length")
st.bar_chart(length_views)
st.caption("Shows which video length ranges generate the highest average views.")

length_engagement = (
    filtered_df.groupby("length_bucket")["engagement_rate"]
    .mean()
)

st.subheader("Average Engagement by Video Length")
st.bar_chart(length_engagement)
st.caption("Shows which video length ranges generate stronger engagement.")

st.divider()

# ROI Analysis
st.header("Production ROI Analysis")

topic_roi = (
    filtered_df.groupby("topic")["views_per_minute"]
    .mean()
    .sort_values(ascending=False)
)

st.subheader("Average ROI Score by Topic")
st.bar_chart(topic_roi)
st.caption("Shows which topics generate the strongest return relative to production effort.")

video_roi = (
    filtered_df.sort_values(
        by="views_per_minute",
        ascending=False
    )
    .head(10)
)

st.subheader("Highest ROI Videos")

roi_table = video_roi[
    [
        "caption",
        "platform",
        "topic",
        "views",
        "editing_time_minutes",
        "views_per_minute",
    ]
].copy()

st.dataframe(roi_table)

st.divider()

# Top Performing Videos
st.header("Top Performing Videos")

top_videos = (
    filtered_df.sort_values(
        by="views",
        ascending=False
    )
    .head(10)
)

top_video_table = top_videos[
    [
        "caption",
        "platform",
        "topic",
        "format",
        "views",
        "engagement_rate"
    ]
].copy()

top_video_table["engagement_rate"] = (
    top_video_table["engagement_rate"] * 100
).round(2)

st.dataframe(top_video_table)

st.caption("Engagement rate is shown as a percentage.")

st.divider()

# Business Recommendations
st.header("Business Recommendations")

st.success("""
1. Prioritize topics and formats with high average views and strong engagement.

2. Use posting pattern analysis to identify better publishing windows.

3. Focus on video lengths that produce both strong reach and engagement.

4. Use ROI analysis to avoid over-investing time into low-return content.

5. Scale content types that generate strong views per minute of editing effort.
""")

st.divider()

# About section
st.header("About This Dashboard")

st.write("""
Built with Python, Pandas, SQLite, SQL, and Streamlit.

This dashboard helps creators identify which content strategies generate
the highest reach, engagement, follower growth, and production ROI.
""")