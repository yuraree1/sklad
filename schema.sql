CREATE TABLE products 
(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	unit VARCHAR(10) NOT NULL,
	min_stock NUMERIC NOT NULL, 
	is_hidden BOOLEAN DEFAULT FALSE NOT NULL,
	CHECK (min_stock>=0)
);


CREATE TABLE stock_movements
(
	id SERIAL PRIMARY KEY,
	product_id INT NOT NULL,
	quantity NUMERIC NOT NULL,
	operation TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
	who TEXT NOT NULL,
	FOREIGN KEY (product_id) REFERENCES products(id),
	CHECK( 
		(operation = 'receipt' AND quantity > 0)
		OR 
		(operation = 'sale' AND quantity < 0)
		)
);