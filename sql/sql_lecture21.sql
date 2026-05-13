-- SELECT * FROM employees_india;
-- SELECT department ,emp_id, AVG(salary) as total   FROM employees_india GROUP BY department,emp_id WITH ROLLUP;
SELECT department ,emp_id, SUM(salary) as total
   FROM employees_india GROUP BY department,emp_id WITH ROLLUP;-- HELP TO FIND THE TOTAL OF THE WHOLE SALARY DATA HERE'
   
