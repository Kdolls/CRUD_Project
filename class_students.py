import mysql.connector
from mysql.connector import Error
import pandas as pd
import School_dataset
import class_CRUD


class CRUD:
    def __init__(self):
        self.connection = None

    def server_connection(self, db_name='School'):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='password',
                db=db_name
            )
            print("Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
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
        if connection.is_connected():
            connection.close()
            print("Connection closed")


class StudentDatabase(CRUD):
    def __init__(self):
        super().__init__()
        self.connection = None
        # self.students = []

    @staticmethod
    def create_student(self, student_id, first_name, last_name, date_of_birth, enrollment_date):
        try:
            query = f"INSERT INTO Students (first_name, last_name, date_of_birth, enrollment_date) VALUES " \
                    f"('{student_id}','{first_name}', '{last_name}', '{date_of_birth}', '{enrollment_date}')"
            create = CRUD()
            create.server_connection()
            create.execute(query)
            print(f"Student {first_name} created successfully.")
        except Error as err:
            print(f"Error: '{err}'")
            return None

    @staticmethod
    def read_all_students():
        try:
            query = "SELECT * FROM Students"
            read = CRUD()
            read.server_connection()
            data = read.read(query)
            print(pd.DataFrame(data))
            print("reading successful.")
        except Error as err:
            print(f"Error: '{err}'")
            return None

    @staticmethod
    def update_student(student_id, new_first_name, new_last_name, new_date_of_birth, new_enrollment_date):
        try:
            query = "UPDATE Students SET first_name, last_name, date_of_birth, enrollment_date WHERE student_id"
            update = CRUD()
            update.server_connection()
            update.execute(query)
            print(f"Student with ID {student_id} updated successfully")
        except Error as err:
            print(f"Error: '{err}'")
            return None

    @staticmethod
    def delete_student(student_id):
        try:
            query = "DELETE FROM Students WHERE student_id"
            delete = CRUD()
            delete.server_connection()
            delete.execute(query)
            print(f"Student with ID {student_id} deleted successfully")
        except Error as err:
            print(f"Error: '{err}'")


# the_new_guy = StudentDatabase()
# # the_new_guy.create_student(22,
# #                            'the new guy',
# #                            'the new guy father',
# #                            '112/23/234',
# #                            '5th of jun')
# the_new_guy.read_all_students()

# print(pd.DataFrame(the_new_guy.read_all_students()))


# print(the_new_guy)

# print(pd.DataFrame(data))

# Example Usage:
connection = CRUD()
connection.server_connection()


def interface():
    if connection:
        try:
            while True:
                print("\nCRUD Operations:")
                print("1. Create Student")
                print("2. Read Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Exit")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    student_id = input("Enter student ID: ")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                    StudentDatabase.create_student(student_id, first_name, last_name, date_of_birth, enrollment_date)

                elif choice == '2':
                    students = StudentDatabase.read_all_students()
                    if students:
                        print("All Students:")
                        for student in students:
                            print(student)
                    else:
                        print("No students found.")

                elif choice == '3':
                    student_id = input("Enter student ID to update: ")
                    new_first_name = input("Enter new first name: ")
                    new_last_name = input("Enter new last name: ")
                    new_date_of_birth = input("Enter new date of birth (YYYY-MM-DD): ")
                    new_enrollment_date = input("Enter new enrollment date (YYYY-MM-DD): ")
                    StudentDatabase.update_student(connection, student_id, new_first_name, new_last_name,
                                                   new_date_of_birth, enrollment_date)

                elif choice == '4':
                    student_id = input("Enter student ID to delete: ")
                    StudentDatabase.delete_student(connection, student_id)

                elif choice == '5':
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")


interface()