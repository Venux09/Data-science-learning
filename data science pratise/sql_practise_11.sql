#here i will practise sql 
-- CREATE DATABASE problem_solving;
-- USE problem_solving;
CREATE TABLE customers(
customer_id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(50)NOT NULL,
city VARCHAR(50) NOT NULL DEFAULT'NULL',
 age INT NOT NULL );
 CREATE TABLE orders (
 order_id INT AUTO_INCREMENT PRIMARY KEY,
 customer_id INT,
 product VARCHAR(100),
 amount INT NOT NULL,
 order_date DATE,
 FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
 ON UPDATE CASCADE
 ON DELETE SET NULL)