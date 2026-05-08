-- starting to practise the learning of the sql 
-- CREATE DATABASE SUBJECTS ;
-- SELECT CURRENT_TIMESTAMP();
SET autocommit = 0;
START TRANSACTION ;
CREATE TABLE SUBJECTESS (
class_id INT AUTO_INCREMENT PRIMARY KEY,
subjects VARCHAR (100));
-- CREATE TABLE students(
-- students_id INT AUTO_INCREMENT PRIMARY KEY ,
-- students_name VARCHAR (100) NOT NULL,
-- student_subject_id INT ,
-- date_joined DATETIME  DEFAULT(CURRENT_TIMESTAMP()),
-- FOREIGN KEY (students_subject_id) REFERENCES SUBJECTS(class_id)
-- ON DELETE SET NULL
-- ON UPDATE CASCADE 
--  );
INSERT INTO SUBJECTES(subjects) VALUES ('Maths','Eng','Science');
INSERT INTO students (students_name,student_subject_id) VALUES 
('ROHAN',1),
('MOHAN',2),
('SOHAN',3);

