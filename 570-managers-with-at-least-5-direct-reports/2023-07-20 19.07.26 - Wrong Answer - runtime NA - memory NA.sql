# Write your MySQL query statement below
SELECT name FROM (
  SELECT name, COUNT(managerID) FROM Employee
) AS c
WHERE name IS NOT NULL;