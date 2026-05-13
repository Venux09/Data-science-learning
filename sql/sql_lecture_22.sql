-- SELECT * FROM employees_india;
-- SELECT * FROM employees_usa;

DELIMITER //

-- CREATE PROCEDURE get_emp_through_id(IN emp_id INT)

-- begin 
-- SELECT * FROM employees_india WHERE emp_id  = emp_id;
-- SELECT * FROM employees_usa WHERE emp_id = emp_id;
-- end //


-- delimiter ; 
-- CALL employees_india_and_usa;
CALL get_emp_by_through(101);

 