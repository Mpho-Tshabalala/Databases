DROP TABLE IF EXISTS Course;

CREATE TABLE Course (
course_code CHAR(5) PRIMARY KEY,
course_name VARCHAR(30) NOT NULL,
course_description text NOT NULL,
teacher_name varchar(30) NOT NULL,
course_level INTEGER CHECK(course_level in (1, 2, 3)) NOT NULL);

INSERT INTO Course 
VALUES
('DS01', 'Python for Data Science', 'This course provides an introductory basis to learning Python.', 'Monty Python', 1),
('DS02', 'Data Analytics and Exploration', 'Techniques for exploring and manipulating data are covered here. This covers reading, converting, visualising, analysing and preprocessing data.', 'Frank Google', 2),
('DS03', 'Machine Learning', 'Introduces students to important machine learning concepts, enabling them to handle big data in a useful manner.', 'Andrew Ng', 3),
('WD01', 'Web Dev Fundamentals', 'Provides a basis to Javascript and all fundamental tools.', 'Mark Zuckerberg', 1),
('WD02', 'Web Dev Frameworks', 'This course aims to provie an understanding of all important frameworks in developing web apps.', 'Zucc Markerberg', 2),
('WD03', 'Client-Server Programming', 'This course challenges students to use what they have learned to build complex web apps.', 'William Gates', 3),
('DB01', 'Files', 'Provides a basis of file inputs and outputs as well as data storage.', 'Sata Drivehard', 1),
('DB02', 'SQL', 'This is the sequel to DB01 - Files.', 'Sata Drivehard', 2),
('DB03', 'Database Management', 'A course on how to be a database admin.', 'Sata Drivehard', 3),
('SE01', 'Introduction to Programming', 'Provides the students with a simple programming language to get the basics.', 'Julia Python', 1),
('SE02', 'Advanced Programming', 'Touches on more advanced algorithms and data structures.', 'Ruby Java', 2),
('SE03', 'Software Engineering', 'An exploration of various development patterns and best practices.', 'Julia Python', 3)