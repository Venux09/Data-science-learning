 --  here we are going to understand how does union works in the sql 
USE harryjoins;
show tables;
SELECT subject FROM marks
UNION ALL
SELECT name FROM students;







