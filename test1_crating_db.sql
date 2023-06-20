CREATE TABLE empl_post_grades
(
employee varchar,
post varchar,
c1 int,
c2 int,
c3 int,
c4 int
);

INSERT INTO empl_post_grades
VALUES
(
'e1' , 'p1', 2, NULL, 3, 2
),
('e2' , 'p3', 3, 2, 1, 1),
('e3' , 'p2', NULL,3,1, NULL),
('e4' , 'p4', 2, 3, NULL, NULL);

CREATE TABLE course_post
(
post varchar,
course1 bool,
course2 bool,
course3 bool,
course4 bool	
);

INSERT INTO course_post
VALUES
(
'p1', TRUE, FALSE, TRUE, FALSE
),
('p2', FALSE, TRUE, TRUE, TRUE),
('p3', FALSE, TRUE, TRUE, FALSE),
('p4', TRUE, TRUE, TRUE, TRUE);


CREATE TABLE c_course
(
course varchar,
c1 bool,
c2 bool,
c3 bool,
c4 bool
);

INSERT INTO c_course
VALUES
('course1', TRUE, NULL, NULL, NULL),
('course2', NULL, NULL, TRUE, NULL),
('course3', NULL, NULL, NULL, TRUE),
('course4', NULL, TRUE, NULL, NULL);

CREATE TABLE c_post
(
post varchar,
c1 int,
c2 int,
c3 int,
c4 int
);


INSERT INTO c_post
VALUES
('p1', 3, NULL, 1, 2),
('p2', NULL, 1,3, NULL),
('p3', 3,3,3,1),
('p4', 2,2, NULL, NULL);
