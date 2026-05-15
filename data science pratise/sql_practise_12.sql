--  here i will be  doing some practise with the union method and also with 
-- CREATE TABLE employees_india(
--     emp_id INT PRIMARY KEY,
--     emp_name VARCHAR(50),
--     department VARCHAR(50),
--     salary DECIMAL(10,2),
--     city VARCHAR(50),
--     joining_date DATE
-- );
-- CREATE TABLE employees_usa(
--     emp_id INT PRIMARY KEY,
--     emp_name VARCHAR(50),
--     department VARCHAR(50),
--     salary DECIMAL(10,2),
--     city VARCHAR(50),
--     joining_date DATE
-- );
--  Inserting some data in the employees_india table 
-- INSERT INTO employees_india VALUES
-- (101, 'Aman', 'IT', 75000, 'Delhi', '2022-01-15'),
-- (102, 'Riya', 'HR', 50000, 'Mumbai', '2021-03-10'),
-- (103, 'Karan', 'Finance', 68000, 'Pune', '2020-07-19'),
-- (104, 'Sneha', 'IT', 82000, 'Bangalore', '2019-11-25'),
-- (105, 'Arjun', 'Marketing', 45000, 'Delhi', '2023-02-01'),
-- (106, 'Meera', 'HR', 54000, 'Chennai', '2022-06-18');
-- inserting some data in the employees_usa tabl

-- inserting data in the employees_usa now
-- INSERT INTO employees_usa VALUES
-- (201, 'John', 'IT', 92000, 'New York', '2021-04-12'),
-- (202, 'Emma', 'Finance', 87000, 'Chicago', '2020-08-30'),
-- (203, 'Michael', 'Marketing', 61000, 'Boston', '2022-01-10'),
-- (204, 'Sophia', 'HR', 58000, 'Seattle', '2019-05-22'),
-- (205, 'David', 'IT', 99000, 'Austin', '2018-12-15'),
-- (206, 'Olivia', 'Finance', 76000, 'San Francisco', '2023-03-08');
-- SELECT * FROM  employees_usa;

-- SELECT * FROM employees_india;
-- SELECT * FROM employees_usa;
-- problem -1 
-- SELECT emp_name , department FROM employees_india
-- UNION 
-- SELECT emp_name , department FROM employees_usa;
-- -- problem -2 
-- SELECT emp_name FROM employees_india 
-- UNION ALL 
-- SELECT emp_name FROM employees_usa ;
-- -- PROBLEM 3 
-- SELECT emp_name,salary  FROM employees_india WHERE  salary>70000
-- UNION 
-- SELECT emp_name,salary   FROM employees_usa WHERE  salary>70000;


-- -- problem 4 
-- SELECT count(emp_id) FROM employees_india ;
-- SELECT count(emp_id) FROM employees_usa ;

-- -- problem 5 
-- SELECT AVG(salary) FROM employees_india;
-- SELECT AVG(salary) FROM employees_usa;

-- -- problem 6 
-- SELECT MIN(salary) , MAX(salary) FROM employees_india;
-- SELECT MIN(salary) , MAX(salary) FROM employees_USa;

-- -- PROBLEM -- 7
-- SELECT emp_name, LENGth(emp_name) FROM employees_india; 
-- SELECT emp_name , LENGTH(emp_name) FROM employees_usa; 

-- problem - 8
-- SELECT * FROM employees_india;
-- SELECT emp_id,emp_name FROM employees_india WHERE joining_date> '2021-12-31';--


-- -- PROBLEM - 9
-- SELECT CONCAT('AMAN WORKS IN ','','IT');

# problems of the view topic 


-- problem 1
-- use practise_set;
-- CREATE VIEW employees_IT AS 
-- SELECT emp_name,salary,department FROM employees_india WHERE department = 'IT';

-- SELECT * FROM employees_IT ;


-- CREATE VIEW global_employees AS 
-- SELECT * FROM employees_india 
-- UNION 
-- SELECT * FROM employees_usa ;


-- SELECT * FROM global_employees;
-- SELECT employees_india info ;
-- UPDATE employees_india SET salary = 0 WHERE salary = salary ;
-- SELECT * FROM global_employees;



-- sql  indexes problems solving 


--  problem number one 
-- use practise_set;
-- CREATE INDEX NAME ON employees_india(emp_name);
-- SHOW INDEX FROM employees_india;
-- PROBLEM - 2 




