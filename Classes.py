import mysql.connector
from mysql.connector import Error
import pandas as pd
import Search


# CRUD connection and execution functions control
class CRUD:
    """
    Class to perform CRUD operations on a MySQL database.
    """

    def __init__(self):
        """
        Constructor method for CRUD class.
        Initializes connection attribute to None.
        """
        self.connection = None

    def server_connection(self, db_name='St_George_college'):
        """
          Establishes connection to the MySQL database.
          db_name (str): The name of the database to connect to. Default is 'St_George_college'.
        """
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
        """
        Executes a SQL query.
        query (str): The SQL query to execute.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except mysql.connector.Error as err:
            print(f"Error: '{err}'")

    def read(self, query):
        """
        Executes a SQL query to retrieve data.
        Parameters: query (str): The SQL query to execute.
        Returns: list: List of tuples containing the retrieved data.
        """
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    def close_connection(self):
        """
        Closes the database connection.
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Connection closed")


# --------------------end-----------------------------


# CRUD application control

# Students CRUD
class Database(CRUD):
    """
    Class to perform CRUD operations on specific database tables.
    """
    def __init__(self):
        """
        Constructor method for Database class.
        Calls parent constructor.
        """
        super().__init__()
        pass

    @staticmethod
    def filter_data(q1, q2, query):
        """
        Filters data from a table based on specified criteria.
        Parameters:
            q1 (str): Table name.
            q2 (str): Column name.
            query (str): Value to filter by.
        """
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
        """
        Creates new student in database
            -student_id (str): The ID of the student to create.
            -first_name (str): Student's first name.
            -last_name (str): Student's last name.
            -date_of_birth (str): Birth date.
            -enrollment_date (str): Course enrollment date.
        """
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
        """
        Reads and displays all Student details in database.
        """
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
        """
        Updates existing student in database.
           -student_id (str): The ID of the student to update.
           -new_first_name (str): New Student's first name.
           -new_last_name (str): New Student's last name.
           -new_date_of_birth (str): New Birth date.
           -new_enrollment_date (str): New Course enrollment date.
       """
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
        """
        Deletes a student record from the database along with related enrollment records.
        student_id (str): The ID of the student to delete.
        """
        try:
            # Delete related enrollment records first
            enrollment_query = f"DELETE FROM Enrollments WHERE student_id = '{student_id}'"
            delete_enrollment = CRUD()
            delete_enrollment.server_connection()
            delete_enrollment.execute(enrollment_query)

            # Then delete the student record
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
        """
        Creates new Teacher in database
            -Teacher_id (str): Create new ID.
            -first_name (str): Teacher's first name.
            -last_name (str): Teacher's last name.
            -date_of_birth (str): Birth date.
            -hire_date (str): Date hired.
        """
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
        """
        Reads and displays all Teacher details in database.
        """
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
        """
        Updates existing Teacher in database.
         -Teacher_id (str): The ID of the teacher to update.
         -new_first_name (str): New teacher's first name.
         -new_last_name (str): New teacher's last name.
         -new_date_of_birth (str): New Birth date.
         -new_hire_date (str): New hire date.
        """
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
        """
        Deletes a teacher record from the database along with related enrollment records.
        teacher_id (str): The ID of the teacher to delete.
        """
        try:
            query = f"DELETE FROM Teachers WHERE teacher_id = '{teacher_id}'"
            delete = CRUD()
            delete.server_connection()
            delete.execute(query)
            print(f"Teacher with ID {teacher_id} deleted successfully")
        except Error as err:
            print(f"Error: '{err}'")

    # --------------------end-----------------------------

    # Courses CRUD
    @staticmethod
    def create_course(course_id, course_name, teacher_id):
        """
        Creates new Course in database
            -course_id (str): Create new course ID.
            -course_name (str): Creates course  name.
            -teacher_id (str): Teacher's id of which course added to.
        """
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
        """
        Reads and displays all Courses details in database.
        """
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
        """
        Updates existing Course in database.
         -course_id (str): Existing course_id to update.
         -new_course_name (str): Creates new course  name.
         -new_teacher_id (str): new Teacher's id of which course added to.
        """
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
        """
        Deletes a Course record from the database.
        course_id (str): The ID of the Course to delete.
        """
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
        """
        Creates new enrollment in database
            -enrollment_id (str): Create new enrollment ID.
            -student_id (str): Enrolls student with id.
            -course_id (str): Adds enrollment to course_id.
            -enrollment_date (str): Enrollment date.
        """
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
        """
        Reads and displays all enrollments details in database.
        """

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
        """
        Updates existing enrollment in database.
            -enrollment_id (str): Updates new enrollment ID.
            -student_id (str): Updates student with id.
            -course_id (str): Updates enrollment to course_id.
            -enrollment_date (str): Updates Enrollment date.
        """
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
        """
        Deletes a Enrollment record from the database.
        enrollment_id (str): The ID of the enroll date to delete.
        """
        try:
            query = f"DELETE FROM Enrollments WHERE id = '{enrollment_id}'"
            delete = CRUD()
            delete.server_connection()
            delete.execute(query)
            print(f"Enrollment with ID {enrollment_id} deleted successfully")
        except Error as err:
            print(f"Error: '{err}'")

# --------------------end-----------------------------
