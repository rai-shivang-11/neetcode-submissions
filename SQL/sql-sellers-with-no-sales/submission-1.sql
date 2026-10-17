-- Write your query below
SELECT seller_name FROM seller
WHERE seller_id not in (SELECT seller_id FROM orders WHERE EXTRACT(YEAR FROM sale_date) = 2020) ORDER BY seller_name