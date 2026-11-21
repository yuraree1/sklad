SELECT SUM(quantity) FROM stock_movements WHERE product_id=1;

SELECT SUM(quantity) FROM stock_movements
WHERE product_id=1 AND created_at <= '2026-09-03';

SELECT COALESCE(SUM(quantity), 0) FROM stock_movements WHERE product_id=99;

SELECT product_id, SUM(quantity) 
FROM stock_movements GROUP BY product_id;

SELECT products.name, SUM(stock_movements.quantity)
FROM stock_movements
JOIN products ON stock_movements.product_id = products.id 
GROUP BY products.id, products.name;

SELECT products.name, COALESCE(SUM(stock_movements.quantity), 0)
FROM products
LEFT JOIN stock_movements ON stock_movements.product_id = products.id 
GROUP BY products.id,  products.name;

SELECT products.name, 
COALESCE(SUM(stock_movements.quantity), 0), products.min_stock
FROM products
LEFT JOIN stock_movements ON stock_movements.product_id = products.id 
GROUP BY products.id, products.name, products.min_stock
HAVING COALESCE(SUM(stock_movements.quantity), 0) <= products.min_stock;