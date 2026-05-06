-- USE practise_db;
-- SHOW TABLES;
-- SELECT * FROM students;
-- updating a table which is called students 
-- UPDATE  students   SET  age = age + 5 WHERE age = age ;
-- SELECT * FROM students;
-- UPDATE students SET age = 18;
-- UPDATE students SET class = 12;
-- SELECT * FROM students;
-- now starting to practise with the deleting methods of the table ;
-- DELETE FROM students WHERE date_of_birth = date_of_birth;
-- SELECT * FROM students ;
SET autocommit = 0 ;

START TRANSACTION ;
-- ALTER TABLE students ADD COLUMN TIME_joined DATETIME DEFAULT(CURRENT_TIMESTAMP());
SELECT * FROM students;
