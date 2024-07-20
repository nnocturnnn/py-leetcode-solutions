# Write your MySQL query statement below
SELECT actor_id, director_id
FROM ActorDirector
WHERE actor_id=director_id
HAVING COUNT(actor_id) >= 3
