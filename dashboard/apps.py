import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(page_title="AttentionLab", layout="wide")

# Load data
df = pd.read_csv("data/cleaned_attentionlab_data.csv")
df["post_date"] = pd.to_datetime(df["post_date"])

# Static chart config
STATIC_CHART_CONFIG = {
    "staticPlot": True,
    "displayModeBar": False
}

# Helper function for static bar charts
def static_bar_chart(data, x_col, y_col, title, x_label=None, y_label=None):
    fig = px.bar(
        data,
        x=x_col,
        y=y_col,
        title=title,
        labels={
            x_col: x_label or x_col,
            y_col: y_label or y_col
        }
    )

    fig.update_layout(
        xaxis_title=x_label or x_col,
        yaxis_title=y_label or y_col
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config=STATIC_CHART_CONFIG
    )

# Title
st.title("AttentionLab")
st.subheader("Creator Intelligence Dashboard")

st.write("""
AttentionLab is an end-to-end analytics dashboard designed to evaluate short-form content performance across TikTok, Instagram Reels, and YouTube Shorts.

The dashboard uses Python, Pandas, SQL, SQLite, and Streamlit to analyze content topics, formats, hooks, posting patterns, video length, engagement, follower growth, and production ROI. The goal is to turn raw creator performance data into clear business recommendations.
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
    .reset_index()
)

static_bar_chart(
    topic_views,
    "topic",
    "views",
    "Average Views by Topic",
    "Topic",
    "Average Views"
)
st.caption("Shows which content topics generate the highest average reach.")

topic_engagement = (
    filtered_df.groupby("topic")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

static_bar_chart(
    topic_engagement,
    "topic",
    "engagement_rate",
    "Average Engagement by Topic",
    "Topic",
    "Average Engagement Rate"
)
st.caption("Shows which topics generate the strongest engagement rate.")

st.divider()

# Format Analysis
st.header("Format Analysis")

format_views = (
    filtered_df.groupby("format")["views"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

static_bar_chart(
    format_views,
    "format",
    "views",
    "Average Views by Format",
    "Format",
    "Average Views"
)
st.caption("Compares how different content formats perform by average views.")

format_engagement = (
    filtered_df.groupby("format")["engagement_rate"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

static_bar_chart(
    format_engagement,
    "format",
    "engagement_rate",
    "Average Engagement by Format",
    "Format",
    "Average Engagement Rate"
)
st.caption("Compares how different formats perform by engagement rate.")

st.divider()

# Hook Analysis
st.header("Hook Analysis")

hook_views = (
    filtered_df.groupby("hook_type")["views"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

static_bar_chart(
    hook_views,
    "hook_type",
    "views",
    "Average Views by Hook Type",
    "Hook Type",
    "Average Views"
)
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
    .reset_index()
)

day_views.columns = ["day_of_week", "views"]

static_bar_chart(
    day_views,
    "day_of_week",
    "views",
    "Average Views by Day of Week",
    "Day of Week",
    "Average Views"
)
st.caption("Shows whether posting day is associated with stronger reach.")

weekend_views = (
    filtered_df.groupby("is_weekend")["views"]
    .mean()
    .reset_index()
)

weekend_views["is_weekend"] = weekend_views["is_weekend"].map({
    True: "Weekend",
    False: "Weekday"
})

static_bar_chart(
    weekend_views,
    "is_weekend",
    "views",
    "Average Views: Weekday vs Weekend",
    "Post Type",
    "Average Views"
)
st.caption("Compares average performance between weekday and weekend posts.")

st.divider()

# Video Length Analysis
st.header("Video Length Analysis")

length_views = (
    filtered_df.groupby("length_bucket")["views"]
    .mean()
    .reset_index()
)

static_bar_chart(
    length_views,
    "length_bucket",
    "views",
    "Average Views by Video Length",
    "Length Bucket",
    "Average Views"
)
st.caption("Shows which video length ranges generate the highest average views.")

length_engagement = (
    filtered_df.groupby("length_bucket")["engagement_rate"]
    .mean()
    .reset_index()
)

static_bar_chart(
    length_engagement,
    "length_bucket",
    "engagement_rate",
    "Average Engagement by Video Length",
    "Length Bucket",
    "Average Engagement Rate"
)
st.caption("Shows which video length ranges generate stronger engagement.")

st.divider()

# Production ROI Analysis
st.header("Production ROI Analysis")

topic_roi = (
    filtered_df.groupby("topic")["views_per_minute"]
    .mean()
    .sort_values(ascending=False)
    .reset_index()
)

static_bar_chart(
    topic_roi,
    "topic",
    "views_per_minute",
    "Average Views Per Minute Worked by Topic",
    "Topic",
    "Views Per Minute Worked"
)
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
        "views_per_minute"
    ]
].copy()

st.dataframe(roi_table)

st.divider()

# Trend Analysis
st.header("Trend Analysis")

views_trend = (
    filtered_df.groupby("post_date")["views"]
    .sum()
    .reset_index()
)

fig_views = px.line(
    views_trend,
    x="post_date",
    y="views",
    title="Views Over Time",
    labels={
        "post_date": "Post Date",
        "views": "Total Views"
    }
)

st.plotly_chart(
    fig_views,
    use_container_width=True,
    config=STATIC_CHART_CONFIG
)

st.caption("Shows how total views changed over time based on posting date.")

engagement_trend = (
    filtered_df.groupby("post_date")["engagement_rate"]
    .mean()
    .reset_index()
)

fig_engagement = px.line(
    engagement_trend,
    x="post_date",
    y="engagement_rate",
    title="Average Engagement Rate Over Time",
    labels={
        "post_date": "Post Date",
        "engagement_rate": "Average Engagement Rate"
    }
)

st.plotly_chart(
    fig_engagement,
    use_container_width=True,
    config=STATIC_CHART_CONFIG
)

st.caption("Shows whether engagement performance is improving or declining over time.")

followers_trend = (
    filtered_df.groupby("post_date")["followers_gained"]
    .sum()
    .cumsum()
    .reset_index()
)

followers_trend.columns = ["post_date", "cumulative_followers_gained"]

fig_followers = px.line(
    followers_trend,
    x="post_date",
    y="cumulative_followers_gained",
    title="Cumulative Followers Gained Over Time",
    labels={
        "post_date": "Post Date",
        "cumulative_followers_gained": "Cumulative Followers Gained"
    }
)

st.plotly_chart(
    fig_followers,
    use_container_width=True,
    config=STATIC_CHART_CONFIG
)

st.caption("Shows follower growth accumulated over time.")

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

# Content Strategy Recommendations
st.header("Content Strategy Recommendations")

best_topic = (
    filtered_df
    .groupby("topic")["views"]
    .mean()
    .idxmax()
)

best_format = (
    filtered_df
    .groupby("format")["engagement_rate"]
    .mean()
    .idxmax()
)

best_hook = (
    filtered_df
    .groupby("hook_type")["views"]
    .mean()
    .idxmax()
)

best_day = (
    filtered_df
    .groupby("day_of_week")["views"]
    .mean()
    .idxmax()
)

best_length = (
    filtered_df
    .groupby("length_bucket")["views"]
    .mean()
    .idxmax()
)

best_roi_topic = (
    filtered_df
    .groupby("topic")["views_per_minute"]
    .mean()
    .idxmax()
)

st.success(
    f"""
    Best Topic: {best_topic}

    Best Format: {best_format}

    Best Hook Type: {best_hook}

    Best Posting Day: {best_day}

    Best Video Length: {best_length}

    Best ROI Topic: {best_roi_topic}
    """
)

st.info(
    f"""
    AttentionLab Recommendation:

    Focus on {best_topic} content using {best_format} formats and {best_hook} hooks.

    Publish primarily on {best_day} and prioritize videos in the {best_length} category.

    The highest production ROI currently comes from {best_roi_topic} content.
    """
)

recommendations = pd.DataFrame({
    "Category": [
        "Topic",
        "Format",
        "Hook Type",
        "Posting Day",
        "Video Length",
        "ROI"
    ],
    "Recommendation": [
        best_topic,
        best_format,
        best_hook,
        best_day,
        best_length,
        best_roi_topic
    ]
})

st.dataframe(recommendations)

st.divider()

# AI Content Strategist
st.header("AI Content Strategist")

st.info(f"""
Recommended Strategy:

Create more **{best_topic}** content using **{best_format}** formats and **{best_hook}** hooks.

Prioritize videos in the **{best_length}** range because they currently generate the strongest average reach.

From a production-efficiency perspective, **{best_roi_topic}** content produces the strongest return based on views per minute of editing time.

This recommendation is generated using rule-based analytics across reach, engagement, posting patterns, and production ROI.
""")

st.divider()

# Content Experiment Tracker
st.header("Content Experiment Tracker")

weekend_winner = (
    "Weekend"
    if filtered_df.groupby("is_weekend")["views"].mean().idxmax()
    else "Weekday"
)

experiments = pd.DataFrame({
    "Experiment": [
        "Best Topic Test",
        "Best Format Test",
        "Best Hook Test",
        "Short vs Long Videos",
        "Weekend vs Weekday Posting"
    ],
    "Winning Segment": [
        best_topic,
        best_format,
        best_hook,
        best_length,
        weekend_winner
    ],
    "Primary Metric": [
        "Average Views",
        "Engagement Rate",
        "Average Views",
        "Average Views",
        "Average Views"
    ],
    "Recommendation": [
        "Scale the strongest topic",
        "Prioritize the highest-engagement format",
        "Use the highest-performing hook style",
        "Focus on the winning length bucket",
        "Post more during the stronger window"
    ]
})

st.dataframe(experiments)

st.caption("This section frames dashboard findings as testable content strategy experiments.")

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
This project demonstrates a complete analytics workflow: data cleaning, feature engineering, SQL analysis, dashboard development, KPI reporting, and recommendation generation.

AttentionLab was built to answer a practical business question: which content strategies produce the strongest engagement and return on production effort?

The dashboard is designed for analyst-style decision making, showing not only what performed well, but also what actions should be taken next.
""")