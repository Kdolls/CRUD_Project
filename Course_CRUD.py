import mysql.connector
from mysql.connector import Error
import pandas as pd
import Classes
import Search
from Classes import Database
from Classes import CRUD

#       connection initialization:
connection = Classes.CRUD()
connection.server_connection()


#       GUI start
def interface():
    if connection:
        try:
            while True:
                print("\nPlease select an Operations: \n")
                print("1. Create Course")
                print("2. Read Courses")
                print("3. Update Course")
                print("4. Delete Course")
                print("5. Return\n")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    course_id = input("Enter course ID: ")
                    course_name = input("Enter course name: ")
                    teacher_id = input("Enter teacher ID: ")
                    Database.create_course(course_id, course_name, teacher_id)

                elif choice == '2':
                    Database.read_all_courses()

                elif choice == '3':
                    course_id = input("Enter course ID to update: ")
                    new_course_name = input("Enter new course name: ")
                    new_teacher_id = input("Enter new teacher ID: ")
                    Database.update_course(course_id, new_course_name, new_teacher_id)

                elif choice == '4':
                    course_id = input("Enter course ID to delete: ")
                    Database.delete_course(course_id)

                elif choice == '5':
                    break

                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
        finally:
            CRUD.close_connection(connection)
    else:
        print("Connection to the database failed.")


if __name__ == "__main__":
    interface()
# --------------------end-----------------------------
