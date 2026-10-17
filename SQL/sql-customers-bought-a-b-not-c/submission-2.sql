-- Write your query below
with pro_a as (
    SELECT * FROM orders WHERE product_name = 'A'
),
pro_b as (
    SELECT * FROM orders WHERE product_name = 'B'
),
pro_c as (
    SELECT * FROM orders WHERE product_name = 'C'
)

SELECT DISTINCT c.customer_id, c.customer_name
FROM customers c
INNER JOIN pro_a a
ON c.customer_id = a.customer_id
INNER JOIN pro_b b
ON c.customer_id = b.customer_id
WHERE c.customer_id not in (SELECT customer_id FROM pro_c)
ORDER BY c.customer_name
