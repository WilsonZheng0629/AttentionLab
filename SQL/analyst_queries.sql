# This query retrieves the top 10 videos with the highest view counts from the 'videos' table, displaying their captions, platforms, and view counts. The results are ordered in descending order based on the number of views.

SELECT caption, platform, topic, format, view
From videos
ORDER BY view DESC
LIMIT 10;

# This query retrieves the top 10 videos with the highest engagement rates from the 'videos' table, displaying their captions, platforms, and engagement rates. The results are ordered in descending order based on the engagement rates.

SELECT caption, platform, topic, format, engagement_rate
From videos
ORDER BY engagement_rate DESC
LIMIT 10;

# This query retrieves the platforms with the highest average view counts from the 'videos' table, displaying their names, video counts, and average views. The results are ordered in descending order based on the average views.

SELECT platform, COUNT(*) as platform_count, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY platform
ORDER BY avg_views DESC;

# This query retrieves the topics with the highest average view counts from the 'videos' table, displaying their names, video counts, and average views. The results are ordered in descending order based on the average views.

SELECT topic, COUNT(*) as topic_count, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY topic
ORDER BY avg_views DESC
;

# This query retrieves the formats with the highest average engagement rates from the 'videos' table, displaying their names, video counts, and average engagement rates. The results are ordered in descending order based on the average engagement rates.

SELECT format, COUNT(*) as format_count, ROUND(AVG(engagement_rate),2) AS avg_engagement_rate
FROM videos
GROUP BY format
ORDER BY avg_engagement_rate DESC;

# This query retrieves the best hook types based on average engagement rates from the 'videos' table, displaying their names, video counts, and average engagement rates. The results are ordered in descending order based on the average engagement rates.

SELECT hook_type, COUNT(*) as hook_type_count, ROUND(AVG(engagement_rate),2) AS avg_engagement_rate
FROM videos
GROUP BY hook_type
ORDER BY avg_engagement_rate DESC;

# This query retrieves the best length buckets based on average engagement rates from the 'videos' table, displaying their names, video counts, and average engagement rates. The results are ordered in descending order based on the average engagement rates.

SELECT length_bucket, COUNT(*) as length_bucket_count, ROUND(AVG(engagement_rate),2) AS avg_engagement_rate
FROM videos
GROUP BY length_bucket
ORDER BY avg_engagement_rate DESC;

# This query retrieves the best posting days based on average engagement rates from the 'videos' table, displaying their names, video counts, and average engagement rates. The results are ordered in descending order based on the average engagement rates.

SELECT day_of_week, COUNT(*) as day_count, ROUND(AVG(engagement_rate),2) AS avg_engagement_rate
FROM videos
GROUP BY day_of_week
ORDER BY avg_engagement_rate DESC;

# This query retrieves the engagement rates and view counts for videos posted on weekends versus weekdays from the 'videos' table, displaying whether the video was posted on a weekend, the count of videos, average engagement rates, and average views. The results are grouped by whether the video was posted on a weekend or not.

SELECT is_weekend, COUNT(*) as weekend_count, ROUND(AVG(engagement_rate),2) AS avg_engagement_rate, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY is_weekend;


# This query retrieves the production ROI information from the 'videos' table, displaying their captions, view counts, editing time, and views per minute worked. The results are ordered in descending order based on the views per minute worked.

SELECT caption, platform, topic, views, editing_time_minutes, ROUND(views_per_minute_worked, 2)
FROM videos
ORDER BY views_per_minute_worked DESC
LIMIT 10;

# This query retrieves the best topics based on follower conversion rates from the 'videos' table, displaying their names, video counts, average follower conversion rates, and total followers gained. The results are ordered in descending order based on the average follower conversion rates.

SELECT
    topic,
    COUNT(*) AS video_count,
    ROUND(AVG(follower_conversion_rate), 4) AS avg_follower_conversion_rate,
    SUM(followers_gained) AS total_followers_gained
FROM videos
GROUP BY topic
ORDER BY avg_follower_conversion_rate DESC;

# This query retrieves the low-effort, high-return videos from the 'videos' table, displaying their captions, platforms, topics, view counts, editing times, and views per minute worked. The results are filtered to include only videos with editing times of 35 minutes or less and are ordered in descending order based on the views per minute worked.

SELECT
    caption,
    platform,
    topic,
    views,
    editing_time_minutes,
    ROUND(views_per_minute_worked, 2) AS views_per_minute_worked
FROM videos
WHERE editing_time_minutes <= 35
ORDER BY views_per_minute_worked DESC
LIMIT 10;