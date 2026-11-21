SELECT SUM(quantity) FROM stock_movements WHERE product_id=1;

SELECT SUM(quantity) FROM stock_movements
WHERE product_id=1 AND created_at <= '2026-09-03';

SELECT COALESCE(SUM(quantity), 0) FROM stock_movements WHERE product_id=99;

