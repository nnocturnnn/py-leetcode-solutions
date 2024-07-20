# Write your MySQL query statement below
SELECT p.product_id, p.product_name 
FROM Product AS p 
LEFT JOIN Sales AS s 
USING (product_id)
WHERE (sale_date BETWEEN '2019-01-01' AND '2019-03-31')
AND p.product_id NOT IN (SELECT DISTINCT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31');

