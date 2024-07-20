# Write your MySQL query statement below
SELECT r.contest_id, ROUND(COUNT(r.user_id) * 100.0 / NULLIF(subquery.total_rows, 0),2) AS percentage
FROM Register r
LEFT JOIN (
    SELECT COUNT(user_id) AS total_rows
    FROM Users
) subquery ON 1=1
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id
