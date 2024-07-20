SELECT
  D.name AS Department,
  E1.name AS Employee,
  E1.salary AS Salary
FROM
  Employee E1
JOIN
  Department D ON E1.departmentId = D.id
WHERE
  (
    SELECT COUNT(DISTINCT E2.salary)
    FROM Employee E2
    WHERE E1.departmentId = E2.departmentId AND E1.salary <= E2.salary
  ) <= 3
ORDER BY
  D.name,
  E1.salary DESC;
