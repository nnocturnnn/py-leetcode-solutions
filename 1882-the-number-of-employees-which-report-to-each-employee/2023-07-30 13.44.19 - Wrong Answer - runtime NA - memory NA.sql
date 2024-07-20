# Write your MySQL query statement below
SELECT employee_id, name, COUNT(reports_to) AS reports_count, ROUND(SUM(age) / COUNT(age)) AS average_age
FROM Employees
HAVING reports_count > 0;