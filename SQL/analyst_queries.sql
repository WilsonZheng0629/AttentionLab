# This query retrieves the top 10 videos with the highest view counts from the 'videos' table, displaying their captions, platforms, and view counts. The results are ordered in descending order based on the number of views.

SELECT caption, platform, view
From videos
ORDER BY view DESC
LIMIT 10;

# This query retrieves the topics with the highest average view counts from the 'videos' table, displaying their names, video counts, and average views. The results are ordered in descending order based on the average views.

SELECT topic, COUNT(*) as topic_count, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY topic
ORDER BY avg_views DESC;

# This query retrieves the formats with the highest average engagement rates from the 'videos' table, displaying their names, video counts, and average engagement rates. The results are ordered in descending order based on the average engagement rates.

SELECT format, COUNT(*) as format_count, ROUND(AVG(engagement_rate),2) AS avg_engagement_rate
FROM videos
GROUP BY format
ORDER BY avg_engagement_rate DESC;

# This query retrieves the platforms with the highest average view counts from the 'videos' table, displaying their names, video counts, and average views. The results are ordered in descending order based on the average views.

SELECT platform, COUNT(*) as platform_count, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY platform
ORDER BY avg_views DESC;

# TThis query retrieves the best hook types based on average views from the 'videos' table, displaying their names, video counts, and average views. The results are ordered in descending order based on the average views.

SELECT hook_type, COUNT(*) as hook_type_count, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY hook_type
ORDER BY avg_views DESC;

# This query retrieves the best length buckets based on average views from the 'videos' table, displaying their names, video counts, and average views. The results are ordered in descending order based on the average views.

SELECT length_bucket, COUNT(*) as length_bucket_count, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY length_bucket
ORDER BY avg_views DESC;

# This query retrieves the best posting days based on average views from the 'videos' table, displaying their names, video counts, and average views. The results are ordered in descending order based on the average views.

SELECT day_of_week, COUNT(*) as day_count, ROUND(AVG(views),2) AS avg_views
FROM videos
GROUP BY day_of_week
ORDER BY avg_views DESC;

# This query retrieves the production ROI information from the 'videos' table, displaying their captions, view counts, editing time, and views per minute worked. The results are ordered in descending order based on the views per minute worked.

SELECT caption, views, editing_time_minutes, ROUND(views_per_minute_worked, 2)
FROM videos
ORDER BY views_per_minute_worked DESC;
