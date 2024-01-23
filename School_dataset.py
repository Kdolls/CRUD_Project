#   Tables
#   Students table
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

#   Sample data
students_values = """
INSERT INTO Students VALUES
    (1, 'John', 'Doe', '2000-01-15', '2022-09-01'),
    (2, 'Jane', 'Smith', '2001-03-22', '2022-09-01'),
    (3, 'Mike', 'Johnson', '2000-12-05', '2022-09-01'
);"""

teachers_values = """
INSERT INTO Teachers VALUES
    (1, 'Dr. Brown', 'Mathews', '1965-05-10', '2005-08-15'),
    (2, 'Prof. White', 'Smith', '1978-12-20', '2010-02-20'),
    (3, 'Dr. Johnson', 'Williams', '1985-08-31', '2018-06-10'
);"""

courses_values = """
INSERT INTO Courses VALUES
    (101, 'Mathematics', 1),
    (102, 'English Literature', 2),
    (103, 'Computer Science', 3
);"""

enrollment_values = """
INSERT INTO Enrollments VALUES
    (1, 1, 101, '2022-09-01'),
    (2, 1, 102, '2022-09-01'),
    (3, 2, 101, '2022-09-01'),
    (4, 2, 103, '2022-09-01'),
    (5, 3, 102, '2022-09-01'
);"""