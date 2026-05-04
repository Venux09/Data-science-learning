-- SHOW TABLES-- \
USE schooldb;
--  SHOW TABLES;
-- SELECT name,age,dat-- e_of_birth from student W-- HERE grade ='10TH';-- this thing are in the order
-- SELECT * -- FROM student WHERE age BETWEEN 12 AND 16 and grade ='10TH' and age != 16;-- 
-- SELECT * FROM student WHERE name LIKE '%nu' ;
-- SELECT * FROM student WHERE date_of_birth IS NOT  NULL;-- 
-- SELECT * FROM student WHERE age = 16 AND date_of_birth IS NOT NULL AND name LIKE '%nu';
SELECT * FROM student WHERE date_of_birth IS NOT NULL  ORDER BY age DESC LIMIT 2,5; -- WE CAN USE LIMIT AND ORDER BY FOR THE ASCENDING AND DESCENDING VALUE IN THE DARTA 



