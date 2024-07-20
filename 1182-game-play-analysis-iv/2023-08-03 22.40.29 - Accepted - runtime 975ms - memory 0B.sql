# Write your MySQL query statement below
SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM (
    SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
    GROUP BY player_id
) AS first_logins
WHERE EXISTS (
    SELECT 1
    FROM Activity
    WHERE player_id = first_logins.player_id
    AND event_date = DATE_ADD(first_login, INTERVAL 1 DAY)
);
