# Write your MySQL query statement below
WITH Q1Sales AS (
    SELECT DISTINCT s.product_id
    FROM Sales s
    WHERE s.sale_date BETWEEN '2019-01-01' AND '2019-03-31'
)

SELECT p.product_id, p.product_name
FROM Product p
JOIN Q1Sales q ON p.product_id = q.product_id
LEFT JOIN Sales s ON p.product_id = s.product_id AND s.sale_date > '2019-03-31'
WHERE s.product_id IS NULL;

