CREATE TABLE IF NOT EXISTS users
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);

INSERT INTO users(name,email)
VALUES
('Greeshma','greeshma@gmail.com'),
('John','john@gmail.com');


CREATE TABLE IF NOT EXISTS products
(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC
);

INSERT INTO products(name,price)
VALUES
('Laptop',65000),
('Mobile',25000),
('Headphones',3000),
('Keyboard',1500);