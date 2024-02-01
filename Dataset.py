#   Tables
#   Students table
import SAND_BOX

students_table = """
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    enrollment_date DATE
);"""

#   Teachers table
teachers_table = """
CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    date_of_birth DATE,
    hire_date DATE
);"""

#   Courses table
courses_table = """
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES Teachers(teacher_id)
);"""

#   Enrollments table
enrollments_table = """
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);"""

# dataset
students_values = """
INSERT INTO Students (student_id, first_name, last_name, date_of_birth, enrollment_date) VALUES
    (1, 'John', 'Doe', '2000-01-15', '2022-09-01'),
    (2, 'Jane', 'Smith', '2001-03-22', '2022-09-01'),
    (3, 'Mike', 'Johnson', '2000-12-05', '2022-09-01'),
    (4, 'Emily', 'Brown', '1999-05-20', '2022-09-01'),
    (5, 'David', 'Williams', '2001-08-10', '2022-09-01'),
    (6, 'Sarah', 'Miller', '2002-06-18', '2022-09-01'),
    (7, 'Michael', 'Taylor', '2000-09-30', '2022-09-01'),
    (8, 'Emma', 'Anderson', '2003-02-12', '2022-09-01'),
    (9, 'Olivia', 'Martinez', '1998-11-25', '2022-09-01'),
    (10, 'Jacob', 'Garcia', '2004-04-05', '2022-09-01');
"""

teachers_values = """
INSERT INTO Teachers (teacher_id, first_name, last_name, date_of_birth, hire_date) VALUES
    (1, 'Dr. Brown', 'Mathews', '1965-05-10', '2005-08-15'),
    (2, 'Prof. White', 'Smith', '1978-12-20', '2010-02-20'),
    (3, 'Dr. Johnson', 'Williams', '1985-08-31', '2018-06-10'),
    (4, 'Mrs. Martinez', 'Garcia', '1970-07-15', '2002-11-30'),
    (5, 'Mr. Thompson', 'Anderson', '1983-04-25', '2015-09-05'),
    (6, 'Dr. Lee', 'Kim', '1976-09-12', '2007-03-18'),
    (7, 'Prof. Adams', 'Jones', '1988-11-03', '2012-07-22'),
    (8, 'Ms. Wilson', 'Taylor', '1990-06-28', '2019-04-10'),
    (9, 'Mr. Clark', 'Brown', '1982-02-17', '2004-10-15'),
    (10, 'Dr. Hernandez', 'Lopez', '1975-10-07', '2008-12-20');
"""

courses_values = """
INSERT INTO Courses (course_id, course_name, teacher_id) VALUES
    (101, 'Mathematics', 1),
    (102, 'English Literature', 2),
    (103, 'Computer Science', 3),
    (104, 'History', 4),
    (105, 'Physics', 5),
    (106, 'Biology', 6),
    (107, 'Chemistry', 7),
    (108, 'Geography', 8),
    (109, 'Art', 9),
    (110, 'Music', 10);
"""

enrollment_values = """
INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES
    (1, 1, 101, '2022-09-01'),
    (2, 1, 102, '2022-09-01'),
    (3, 2, 101, '2022-09-01'),
    (4, 2, 103, '2022-09-01'),
    (5, 3, 102, '2022-09-01'),
    (6, 3, 104, '2022-09-01'),
    (7, 4, 103, '2022-09-01'),
    (8, 4, 105, '2022-09-01'),
    (9, 5, 101, '2022-09-01'),
    (10, 5, 106, '2022-09-01');
"""

# connection initialisation
read_me = SAND_BOX.StudentDatabase()
read_me.server_connection()
write_me = SAND_BOX.CRUD()
write_me.server_connection()

# write table
# write_me.execute(teachers_table)
# write_me.execute(courses_table)
# write_me.execute

# write values
# write_me.execute(teachers_values)
# write_me.execute(courses_values)
# write_me.execute(enrollment_values)


print(read_me.read("SELECT * FROM Enrollments"))
