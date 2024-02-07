import mysql.connector
from mysql.connector import Error
import pandas as pd
import Classes
import Course_CRUD
import Enroll_CRUD
import Search
import Student_CRUD
import Teacher_CRUD
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
                print("\n1. Student operations ")
                print("2. Teacher operations ")
                print("3. Course operations ")
                print("4. Enrollments operations ")
                print("5. Search")
                print("6. Exit\n")

                choice = input("Enter your choice (1-5): ")
                # instance call for each available interface
                if choice == '1':
                    Student_CRUD.interface()
                elif choice == '2':
                    Teacher_CRUD.interface()
                elif choice == '3':
                    Course_CRUD.interface()
                elif choice == '4':
                    Enroll_CRUD.interface()
                elif choice == '5':
                    search = Search.Search()
                    chosen_category = search.menu_A()
                    current_list = None
                    if chosen_category == "Students":
                        current_list = search.list_student
                    elif chosen_category == "Teachers":
                        current_list = search.list_teacher
                    elif chosen_category == "Courses":
                        current_list = search.list_course
                    elif chosen_category == "Enrollments":
                        current_list = search.list_enroll

                    chosen_keyword = search.menu_B(chosen_category, current_list)
                    search.menu_C()
                    Database.filter_data(chosen_category, chosen_keyword, choice)

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


if __name__ == "__main__":
    interface()
# --------------------end-----------------------------
