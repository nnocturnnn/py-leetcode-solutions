# Write your MySQL query statement below
SELECT class FROM (
SELECT class, COUNT(class) AS c
FROM Courses
GROUP BY class
HAVING c>5
) AS t