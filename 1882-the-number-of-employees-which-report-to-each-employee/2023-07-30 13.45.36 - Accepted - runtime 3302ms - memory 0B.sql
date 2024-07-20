# Write your MySQL query statement below
SELECT
    manager.employee_id,
    manager.name,
    COUNT(employee.employee_id) AS reports_count,
    ROUND(AVG(employee.age), 0) AS average_age
FROM
    Employees AS manager
LEFT JOIN
    Employees AS employee
ON
    manager.employee_id = employee.reports_to
GROUP BY
    manager.employee_id,
    manager.name
HAVING
    COUNT(employee.employee_id) >= 1
ORDER BY
    manager.employee_id;
