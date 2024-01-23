import mysql.connector
from mysql.connector import Error
import pandas as pd


# SQL server connection function
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            db='school'
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


# DATABASE creation function
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")


# Query execution function
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


#                       FUNCTION CALL
link = create_server_connection('localhost', 'root', 'password')
# create_database(connection,'CREATE DATABASE school')


# tables

students_table = """  
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birth_date DATE,
    enrollment_date DATE
);"""

teachers_table = """
CREATE TABLE Teachers (
    teacher_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hire_date DATE
);"""

courses_table = """
CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    instructor_id INT,
    FOREIGN KEY (instructor_id) REFERENCES Teachers(teacher_id)
);"""


enrollments_table = """
CREATE TABLE Enrollments (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    classroom_id INT,
    enrollment_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id),
    FOREIGN KEY (classroom_id) REFERENCES Classrooms(classroom_id)
);"""

grades_table = """
CREATE TABLE Grades (
    grade_id INT PRIMARY KEY,
    enrollment_id INT,
    grade CHAR(1),
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(enrollment_id)
);"""

sample_data_teacher = """
    (1, 'Dr. Brown', 'Mathews', '2005-08-15'),
    (2, 'Prof. White', 'Smith', '2010-02-20'),
    (3, 'Dr. Johnson', 'Williams', '2018-06-10');
"""

sample_data_classrooms = """
    (1, '101'),
    (2, '102'),
    (3, '201');
"""
sample_data_courses_values = """
    (101, 'Mathematics', 1),
    (102, 'English Literature', 2),
    (103, 'Computer Science', 3);
"""

sample_data_students_values = """
INSERT INTO Students VALUES
    (1, 'John', 'Doe', '2000-01-15', '2022-09-01'),
    (2, 'Jane', 'Smith', '2001-03-22', '2022-09-01'),
    (3, 'Mike', 'Johnson', '2000-12-05', '2022-09-01');
"""
sample_data_enrollments = """
INSERT INTO Enrollments VALUES
    (1, 1, 101, 1, '2022-09-01'),
    (2, 1, 102, 2, '2022-09-01'),
    (3, 2, 101, 3, '2022-09-01'),
    (4, 2, 103, 1, '2022-09-01'),
    (5, 3, 102, 2, '2022-09-01');
"""

sample_data_grades = """
INSERT INTO Grades VALUES
    (1, 1, 'A'),
    (2, 2, 'B'),
    (3, 3, 'B+'),
    (4, 4, 'A-'),
    (5, 5, 'C');
"""

