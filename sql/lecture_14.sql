-- CREATE DATABASE school;
-- USE school;
-- CREATE TABLE classes (
-- class_id INT AUTO_INCREMENT PRIMARY KEY ,
-- class_name VARCHAR(50)
-- );
-- CREATE TABLE students_table (

-- student_id INT AUTO_INCREMENT PRIMARY KEY,
-- student_nameS VARCHAR(100) NOT NULL,
-- class_id INT,
-- FOREIGN KEY (class_id) REFERENCES classes(class_id) 
-- ON UPDATE CASCADE  
-- ON DELETE SET NULL   );
-- INSERT INTO classes (class_name) VALUES ('Mathematics'), ('Science'), ('History');
-- INSERT INTO students_table (student_nameS,class_id) VALUES 
-- ('Alice',1),
-- ('BOb',2),
-- ('Charlie', 3);
-- SELECT * FROM students_table;
-- SELECT * FROM classes;
-- DELETE FROM classes WHERE  class_id = 2;
-- SELECT * FROM students_table;
-- UPDATE classes SET class_id = 2 WHERE class_id = NULL;
-- UPDATE classes SET class_id = 101 WHERE class_id = 1;
-- UPDATE classes SET class_id = 102 WHERE class_id = 2;
-- UPDATE classes SET class_id = 103 WHERE class_id = 3;
-- SELECT * FROM classes ;
-- SHOW CREATE TABLE  students_table;

SELECT 
    table_name, 
    column_name, 
    constraint_name, 
    referenced_table_name, 
    referenced_column_name
FROM 
    information_schema.key_column_usage
WHERE 
    referenced_table_name IS NOT NULL
    AND table_schema = 'school';
