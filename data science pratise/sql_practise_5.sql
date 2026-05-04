use practise_db;
-- CREATE TABLE students (
-- id INT PRIMARY KEY,
-- name VARCHAR(100),
-- class INT ,
-- date_of_birth DATE ,
-- course VARCHAR (100));
-- INSERT INTO students (id,name,class,date_of_birth,course) VALUES
-- (1, 'Aarav Sharma', 12, '2007-03-12', 'PCM'),
-- (2, 'Vivaan Gupta', 11, '2008-07-25', 'PCB'),
-- (3, 'Aditya Singh', 12, '2007-11-05', 'Commerce'),
-- (4, 'Arjun Verma', 10, '2009-01-18', 'Science'),
-- (5, 'Sai Kumar', 11, '2008-06-22', 'PCM'),
-- (6, 'Krishna Patel', 12, '2007-09-14', 'Arts'),
-- (7, 'Rohan Das', 10, '2009-12-03', 'Science'),
-- (8, 'Karan Mehta', 11, '2008-02-27', 'Commerce'),
-- (9, 'Rahul Nair', 12, '2007-08-19', 'PCM'),
-- (10, 'Ankit Yadav', 10, '2009-04-10', 'Science'),

-- (11, 'Mohit Joshi', 11, '2008-10-01', 'PCB'),
-- (12, 'Neeraj Sharma', 12, '2007-05-06', 'Commerce'),
-- (13, 'Suresh Reddy', 10, '2009-07-30', 'Science'),
-- (14, 'Varun Kapoor', 11, '2008-03-16', 'PCM'),
-- (15, 'Deepak Mishra', 12, '2007-06-28', 'Arts'),
-- (16, 'Rajat Jain', 10, '2009-11-11', 'Science'),
-- (17, 'Aman Khan', 11, '2008-09-09', 'Commerce'),
-- (18, 'Nikhil Arora', 12, '2007-02-21', 'PCM'),
-- (19, 'Harsh Vardhan', 10, '2009-08-08', 'Science'),
-- (20, 'Yash Thakur', 11, '2008-12-14', 'PCB'),

-- (21, 'Manish Choudhary', 12, '2007-04-04', 'Commerce'),
-- (22, 'Ravi Teja', 10, '2009-03-29', 'Science'),
-- (23, 'Kunal Sinha', 11, '2008-11-23', 'PCM'),
-- (24, 'Shubham Goyal', 12, '2007-01-30', 'Arts'),
-- (25, 'Tarun Bansal', 10, '2009-06-17', 'Science'),
-- (26, 'Vikas Yadav', 11, '2008-05-13', 'Commerce'),
-- (27, 'Abhishek Pandey', 12, '2007-10-19', 'PCM'),
-- (28, 'Lokesh Singh', 10, '2009-09-02', 'Science'),
-- (29, 'Gaurav Saxena', 11, '2008-08-26', 'PCB'),
-- (30, 'Ritesh Agarwal', 12, '2007-07-07', 'Commerce'),

-- (31, 'Sameer Ansari', 10, '2009-02-12', 'Science'),
-- (32, 'Pankaj Verma', 11, '2008-04-18', 'PCM'),
-- (33, 'Dinesh Kumar', 12, '2007-12-01', 'Arts'),
-- (34, 'Ashish Tiwari', 10, '2009-10-20', 'Science'),
-- (35, 'Rohit Sharma', 11, '2008-01-05', 'Commerce'),
-- (36, 'Sanjay Gupta', 12, '2007-06-09', 'PCM'),
-- (37, 'Alok Mishra', 10, '2009-05-25', 'Science'),
-- (38, 'Vivek Singh', 11, '2008-03-03', 'PCB'),
-- (39, 'Prateek Jain', 12, '2007-08-11', 'Commerce'),
-- (40, 'Sunil Yadav', 10, '2009-07-15', 'Science'),

-- (41, 'Kishan Lal', 11, '2008-09-28', 'PCM'),
-- (42, 'Om Prakash', 12, '2007-02-14', 'Arts'),
-- (43, 'Devendra Singh', 10, '2009-11-06', 'Science'),
-- (44, 'Ramesh Gupta', 11, '2008-06-30', 'Commerce'),
-- (45, 'Mukesh Kumar', 12, '2007-03-08', 'PCM'),
-- (46, 'Ajay Yadav', 10, '2009-01-22', 'Science'),
-- (47, 'Bharat Singh', 11, '2008-12-19', 'PCB'),
-- (48, 'Naresh Sharma', 12, '2007-05-27', 'Commerce'),
-- (49, 'Mahesh Patel', 10, '2009-08-13', 'Science'),
-- (50, 'Sandeep Verma', 11, '2008-07-04', 'PCM');

-- UPDATE students SET age = 19 WHERE id IN (1,3,6,9,12,15,18,21,24,27,30,33,36,39,42,45,48);

-- UPDATE students SET age = 18 WHERE id IN (2,5,8,11,14,17,20,23,26,29,32,35,38,41,44,47,50);

-- UPDATE students SET age = 16 WHERE id IN (4,7,10,13,16,19,22,25,28,31,34,37,40,43,46,49);   
SELECT * FROM students;