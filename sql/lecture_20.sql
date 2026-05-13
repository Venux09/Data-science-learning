# here i am going to understood the subquiries in the sql 
-- SELECT emp_name,department,salary FROM employees_india
-- WHERE salary > (SELECT AVG(salary) FROM  employees_india);

SELECT emp_name, salary,department FROM EMPLOYEES_INDIA AS E -- 
Where salary >( 
SELECT AVG(salary) FROM employees Where department = e.department );