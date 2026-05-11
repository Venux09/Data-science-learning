-- HERE WE WILL UNDERSTAND HOW TO USE THE BUILT IN FUNCTION OF THE MYSQL 
-- SELECT CONCAT(id,' ',name ) as  name FROM students;
-- SELECT NOW();
-- SELECT name , (length(name)) as len FROM students; 
SELECT DATADIFF(NOW(),id) as days  FROM students;