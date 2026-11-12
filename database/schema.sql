CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(100),
    price NUMERIC
);

INSERT INTO products(name,category,price)
VALUES
('iPhone 16','Mobile',85000),
('Samsung S24','Mobile',70000),
('Dell Inspiron','Laptop',60000);