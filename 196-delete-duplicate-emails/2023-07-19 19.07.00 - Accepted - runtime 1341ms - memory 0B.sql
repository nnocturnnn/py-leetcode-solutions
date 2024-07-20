# Write your MySQL query statement below
DELETE p1
FROM Person p1
LEFT JOIN (
    SELECT email, MIN(id) AS min_id
    FROM Person
    GROUP BY email
) p2 ON p1.email = p2.email AND p1.id > p2.min_id
WHERE p2.email IS NOT NULL;