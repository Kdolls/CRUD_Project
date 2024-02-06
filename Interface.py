import mysql.connector
from mysql.connector import Error
import pandas as pd
import Classes
import Search
from Classes import StudentDatabase
from Classes import CRUD


#       connection initialization:
connection = Classes.CRUD()
connection.server_connection()


#       GUI start
def interface():
    if connection:
        try:
            while True:
                print("\nCRUD Operations:")
                print("1. Create Student")
                print("2. Read Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Search")
                print("6. Exit")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    student_id = input("Enter student ID: ")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                    StudentDatabase.create_student(student_id, first_name, last_name, date_of_birth, enrollment_date)

                elif choice == '2':
                    StudentDatabase.read_all_students()

                elif choice == '3':
                    student_id = input("Enter student ID to update: ")
                    new_first_name = input("Enter new first name: ")
                    new_last_name = input("Enter new last name: ")
                    new_date_of_birth = input("Enter new date of birth in form of (YYYY-MM-DD): ")
                    new_enrollment_date = input("Enter new enrollment date in form of (YYYY-MM-DD): ")
                    StudentDatabase.update_student(student_id, new_first_name, new_last_name,
                                                   new_date_of_birth, new_enrollment_date)

                elif choice == '4':
                    student_id = input("Enter student ID to delete: ")
                    StudentDatabase.delete_student(student_id)

                elif choice == '5':
                    q2 = Search.Search()
                    q3 = Search.Search()
                    StudentDatabase.filter_data(q2.menu_B(), q3.menu_C())

                elif choice == '6':
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
        finally:
            CRUD.close_connection(connection)
    else:
        print("Connection to the database failed.")


interface()
# --------------------end-----------------------------

# testing = StudentDatabase()
# testing.server_connection()
# testing.filter_data(343)
