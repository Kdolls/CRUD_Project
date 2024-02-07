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
                print("1. Create Enrollment")
                print("2. Read Enrollments")
                print("3. Update Enrollment")
                print("4. Delete Enrollment")
                print("5. Return\n")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    enrollment_id = input("Enter enrollment ID: ")
                    student_id = input("Enter student ID: ")
                    course_id = input("Enter course ID: ")
                    enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                    Database.create_enrollment(enrollment_id, student_id, course_id, enrollment_date)

                elif choice == '2':
                    Database.read_all_enrollments()

                elif choice == '3':
                    enrollment_id = input("Enter enrollment ID to update: ")
                    new_student_id = input("Enter new student ID: ")
                    new_course_id = input("Enter new course ID: ")
                    new_enrollment_date = input("Enter new enrollment date (YYYY-MM-DD): ")
                    Database.update_enrollment(enrollment_id, new_student_id, new_course_id, new_enrollment_date)

                elif choice == '4':
                    enrollment_id = input("Enter enrollment ID to delete: ")
                    Database.delete_enrollment(enrollment_id)

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
