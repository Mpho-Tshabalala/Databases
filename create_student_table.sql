DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
student_id CHAR(13) PRIMARY KEY,
first_name VARCHAR(30) NOT NULL,
last_name VARCHAR(30) NOT NULL,
email varchar(30) NOT NULL,
stu_subject_code CHAR(5) NOT NULL,
mark INTEGER NOT NULL,

FOREIGN KEY(stu_subject_code) REFERENCES Course(course_code));

INSERT INTO Student 
VALUES
('JV00100200304', 'Johnny', 'Valker', 'jv@email.com', 'DS02', 64),
('JS00100200305', 'Jack', 'Sparrow', 'js@blackpearl.com', 'WD01', 52),
('LM00100200306', 'Luffy', 'Monkey', 'pking@linegrand.com', 'WD03', 43),
('PA00100200307', 'Paul', 'Atreides', 'paul@melange.com', 'DS01', 78),
('LA00100200308', 'Leto', 'Atreides', 'leto@melange.com', 'DS03', 92),
('AT00100200309', 'Alan', 'Turing', 'whereis@myemail.com', 'SE01', 72),
('AL00100200310', 'Ada', 'Lovelace', 'motherof@computing.com', 'SE03', 86),
('PP00100200311', 'Peter', 'Parker', 'pp@marvel.com', 'WD03', 83),
('AS00100200312', 'Anthony', 'Stark', 'ironman@marvel.com', 'SE02', 95),
('KK00100200313', 'Kamala', 'Khan', 'ms@marvel.com', 'DS01', 67),
('CD00100200314', 'Carol', 'Danvers', 'captain@marvel.com', 'WD02', 72),
('DV00100200315', 'Darth', 'Vader', 'dv@deathstar.com', 'SE03', 62),
('AS00100200316', 'Anakin', 'Skywalker', 'ihatesand@deathstar.com', 'SE02', 62),
('LS00100200317', 'Leia', 'Skywalker', 'leader@rebels.com', 'DS03', 89),
('OK00100200318', 'Obi-Wan', 'Kenobi', 'hellothere@jedicouncil.com', 'DS01', 70),
('GG00100200319', 'Gandalf', 'Grey', 'youshall@notpass.com', 'WD02', 27),
('JB00100200320', 'Johnny', 'Bravo', 'jb@cn.com', 'DB02', 69),
('PB00100200321', 'Pinky', 'Brain', 'pinky@brain.com', 'DS01', 100),
('JS00100200322', 'John', 'Smith', 'doctor@who.com', 'DB03', 79),
('JS00100200323', 'Jane', 'Smith', 'professor@who.com', 'DB03', 92),
('EP00100200324', 'Elvis', 'Presley', 'elvis@elvis.com', 'SE01', 56),
('FM00100200325', 'Frederick', 'Mercury', 'rhapsody@queen.com', 'WD03', 87),
('BC00100200326', 'Benedict', 'Cumberbatch', 'benny@strange.com', 'DB01', 65),
('WT00100200327', 'Wimbledon', 'Tennismatch', 'wimbeldon@strange.com', 'DB02', 68)