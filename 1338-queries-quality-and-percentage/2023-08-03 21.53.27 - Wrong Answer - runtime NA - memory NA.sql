# Write your MySQL query statement below
SELECT query_name, ROUND(SUM(q) / COUNT(*),2) AS quality,
  ROUND(COUNT(CASE WHEN rating<3 THEN query_name ELSE NULL END) / COUNT(*),2) * 100 AS poor_query_percentage
FROM (SELECT query_name, rating, ROUND((rating / position), 2) AS q
FROM Queries) qu
GROUP BY query_name