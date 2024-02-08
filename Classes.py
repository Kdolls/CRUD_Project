import mysql.connector
from mysql.connector import Error
import pandas as pd
import Search


#   CRUD connection and execution functions control
class CRUD:
    def __init__(self):
        self.connection = None

    def server_connection(self, db_name='St_George_college'):

        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='password',
                db=db_name
            )
            # print("Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")

    def read(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")


# --------------------end-----------------------------


#   CRUD application control

# Students CRUD
class Database(CRUD):
    def __init__(self):
        super().__init__()
        pass

    @staticmethod
    def filter_data(q1, q2, query):
        try:
            request = f"SELECT * FROM {q1} WHERE {q2} = '{query}'"
            read = CRUD()
            read.server_connection()
            data = read.read(request)
            print(pd.DataFrame(data))
            print(f"{q1} with {q2} {query} filtered successfully")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def create_student(student_id, first_name, last_name, date_of_birth, enrollment_date):
        try:
            query = f"INSERT INTO Students (student_id, first_name, last_name, date_of_birth, enrollment_date) VALUES " \
                    f"('{student_id}', '{first_name}', '{last_name}', '{date_of_birth}', '{enrollment_date}')"
            create = CRUD()
            create.server_connection()
            create.execute(query)
            print(f"Student {first_name} created successfully.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def read_all_students():
        try:
            query = "SELECT * FROM Students"
            read = CRUD()
            read.server_connection()
            data = read.read(query)
            print(pd.DataFrame(data))
            print("Reading successful.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def update_student(student_id, new_first_name, new_last_name, new_date_of_birth, new_enrollment_date):
        try:
            query = f"UPDATE Students SET first_name = '{new_first_name}', last_name = '{new_last_name}', " \
                    f"date_of_birth = '{new_date_of_birth}', enrollment_date = '{new_enrollment_date}' " \
                    f"WHERE student_id = '{student_id}'"
            update = CRUD()
            update.server_connection()
            update.execute(query)
            print(f"Student with ID {student_id} updated successfully")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def delete_student(student_id):
        try:
            query = f"DELETE FROM Students WHERE student_id = '{student_id}'"
            delete = CRUD()
            delete.server_connection()
            delete.execute(query)
            print(f"Student with ID {student_id} deleted successfully")
        except Error as err:
            print(f"Error: '{err}'")

    # --------------------end-----------------------------

    # Teachers CRUD
    @staticmethod
    def create_teacher(teacher_id, first_name, last_name, date_of_birth, hire_date):
        try:
            query = f"INSERT INTO Teachers (teacher_id, first_name, last_name, date_of_birth, hire_date) VALUES " \
                    f"('{teacher_id}', '{first_name}', '{last_name}', '{date_of_birth}', '{hire_date}')"
            create = CRUD()
            create.server_connection()
            create.execute(query)
            print(f"Teacher {first_name} created successfully.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def read_all_teachers():
        try:
            query = "SELECT * FROM Teachers"
            read = CRUD()
            read.server_connection()
            data = read.read(query)
            print(pd.DataFrame(data))
            print("Reading successful.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def update_teacher(teacher_id, new_first_name, new_last_name, new_date_of_birth, new_hire_date):
        try:
            query = f"UPDATE Teachers SET first_name = '{new_first_name}', last_name = '{new_last_name}', " \
                    f"date_of_birth = '{new_date_of_birth}', hire_date = '{new_hire_date}' " \
                    f"WHERE teacher_id = '{teacher_id}'"
            update = CRUD()
            update.server_connection()
            update.execute(query)
            print(f"Teacher with ID {teacher_id} updated successfully")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def delete_teacher(teacher_id):
        try:
            query = f"DELETE FROM Teachers WHERE teacher_id = '{teacher_id}'"
            delete = CRUD()
            delete.server_connection()
            delete.execute(query)
            print(f"Student with ID {teacher_id} deleted successfully")
        except Error as err:
            print(f"Error: '{err}'")

    # --------------------end-----------------------------

    # Courses CRUD
    @staticmethod
    def create_course(course_id, course_name, teacher_id):
        try:
            query = f"INSERT INTO Courses (course_id, course_name, course_description, instructor_id) VALUES " \
                    f"('{course_id}', '{course_name}', '{teacher_id}')"
            create = CRUD()
            create.server_connection()
            create.execute(query)
            print(f"Course {course_name} created successfully.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def read_all_courses():
        try:
            query = "SELECT * FROM Courses"
            read = CRUD()
            read.server_connection()
            data = read.read(query)
            print(pd.DataFrame(data))
            print("Reading successful.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def update_course(course_id, new_course_name, new_teacher_id):
        try:
            query = f"UPDATE Courses SET course_name = '{new_course_name}'," \
                    f"teacher_id = '{new_teacher_id}', " \
                    f"WHERE course_id = '{course_id}'"
            update = CRUD()
            update.server_connection()
            update.execute(query)
            print(f"Course with ID {course_id} updated successfully")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def delete_course(course_id):
        try:
            query = f"DELETE FROM Courses WHERE teacher_id = '{course_id}'"
            delete = CRUD()
            delete.server_connection()
            delete.execute(query)
            print(f"Courses with ID {course_id} deleted successfully")
        except Error as err:
            print(f"Error: '{err}'")

    # --------------------end-----------------------------

    # Enrollment CRUD

    @staticmethod
    def create_enrollment(enrollment_id, student_id, course_id, enrollment_date):
        try:
            query = f"INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) " \
                    f"VALUES ('{enrollment_id}', '{student_id}', '{course_id}', '{enrollment_date}')"
            create = CRUD()
            create.server_connection()
            create.execute(query)
            print("Enrollment created successfully.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def read_all_enrollments():
        try:
            query = "SELECT * FROM Enrollments"
            read = CRUD()
            read.server_connection()
            data = read.read(query)
            print(pd.DataFrame(data))
            print("Reading successful.")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def update_enrollment(enrollment_id, new_student_id, new_course_id, new_enrollment_date):
        try:
            query = (f"UPDATE Enrollments SET new_student_id = '{new_student_id}', new_course_id = '{new_course_id}',"
                     f"new_enrollment_date = '{new_enrollment_date}' "
                     f" WHERE enrollment_id = '{enrollment_id}'")
            update = CRUD()
            update.server_connection()
            update.execute(query)
            print(f"Enrollment with ID {enrollment_id} updated successfully")
        except Error as err:
            print(f"Error: '{err}'")

    @staticmethod
    def delete_enrollment(enrollment_id):
        try:
            query = f"DELETE FROM Enrollments WHERE id = '{enrollment_id}'"
            delete = CRUD()
            delete.server_connection()
            delete.execute(query)
            print(f"Enrollment with ID {enrollment_id} deleted successfully")
        except Error as err:
            print(f"Error: '{err}'")

# --------------------end-----------------------------
