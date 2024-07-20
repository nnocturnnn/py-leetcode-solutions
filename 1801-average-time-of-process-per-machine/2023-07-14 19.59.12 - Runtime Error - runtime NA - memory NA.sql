# Write your MySQL query statement below
SELECT machine_id, ROUND(AVG(end - start), 3) AS processing_time
FROM your_table_name
GROUP BY machine_id;