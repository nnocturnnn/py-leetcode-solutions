SELECT employee_id 
FROM (
SELECT Employees.employee_id, name, salary
FROM Employees
LEFT JOIN Salaries ON Employees.employee_id = Salaries.employee_id

UNION

SELECT Salaries.employee_id, name, salary
FROM Employees
RIGHT JOIN Salaries ON Employees.employee_id = Salaries.employee_id
) AS  sub
WHERE name IS NULL OR salary IS NULL
ORDER BY employee_id