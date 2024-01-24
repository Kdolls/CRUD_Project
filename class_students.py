import mysql.connector
from mysql.connector import Error
import pandas as pd
import School_dataset


class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, enrollment_date):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.enrollment_date = enrollment_date


class StudentDatabase:
    def __init__(self):
        self.students = []

    def create_student(self, student_id, first_name, last_name, date_of_birth, enrollment_date):
        new_student = Student(self, student_id, first_name, last_name, date_of_birth, enrollment_date)
        self.students.append(new_student)
        print(f"Student {first_name} created successfully.")

    def read_all_students(self):
        for student in self.students:
            print(f"ID: {student.student_id}, "
                  f"Name: {student.first_name}, "
                  f"last Name: {student.last_name},"
                  f"Date of Birth: {student.date_of_birth}, "
                  f"Enrollment date: {student.enrollment_date}")

    def read_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(f"ID: {student.student_id}, "
                      f"Name: {student.first_name}, "
                      f"last Name: {student.last_name},"
                      f"Enrollment date: {student.enrollment_date}")
                return
        print(f"Student with ID {student_id} not found.")

    def update_student(self, student_id, new_name, new_age, new_grade):
        for student in self.students:
            if student.student_id == student_id:
                student.first_name = new_name
                student.date_of_birth = new_age
                print(f"Student {student.name} updated successfully.")
                return
        print(f"Student with ID {student_id} not found.")

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                del self.students[i]
                print(f"Student with ID {student_id} deleted successfully.")
                return
        print(f"Student with ID {student_id} not found.")
