# Write your MySQL query statement below
SELECT project_id, SUM(experience_years) / COUNT(experience_years) AS average_years
FROM Project AS p
LEFT JOIN Employee AS e
ON p.employee_id=e.employee_id
GROUP BY project_id