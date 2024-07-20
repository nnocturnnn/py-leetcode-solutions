# Write your MySQL query statement below
SELECT MAX(num) AS num FROM (
SELECT num, COUNT(num) AS c FROM MyNumbers
GROUP BY num
HAVING c=1
) AS sub