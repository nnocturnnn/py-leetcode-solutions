# Write your MySQL query statement below
SELECT class FROM (
SELECT class, COUNT(class) AS c
FROM Courses
GROUP BY class
HAVING c>4
) AS t