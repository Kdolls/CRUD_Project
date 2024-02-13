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
from Sorted import Filter_me
import Quick_sort

# connection initialization:
connection = Classes.CRUD()
connection.server_connection()


# GUI start
def interface():
    """
    Main user interface for the database.
    Displays options for CRUD operations on different entities and handles user input.
    """
    if connection:
        try:
            while True:
                # Quick sort testing instance------------------------------------------
                print('\n0. For A Sorted view click me!\n')

                print("1. Student operations ")
                print("2. Teacher operations ")
                print("3. Course operations ")
                print("4. Enrollments operations ")
                print("5. Search")
                print("6. Exit\n")

                choice = input("Welcome to St_George_college database management tool.\n Please "
                               "Enter your choice from menu above: ")
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

                    search_keyword = search.menu_B(chosen_category, current_list)
                    credential = search.menu_C()
                    Database.filter_data(chosen_category, search_keyword, credential)

                # Quick sort testing-------------------------------------------------------

                elif choice == '0':
                    search = Search.Search()
                    chosen_category = search.menu_A()

                    if chosen_category == "Students":
                        current_list = search.list_student
                    elif chosen_category == "Teachers":
                        current_list = search.list_teacher
                    elif chosen_category == "Courses":
                        current_list = search.list_course
                    elif chosen_category == "Enrollments":
                        current_list = search.list_enroll

                    print(Filter_me.sort_all_data(chosen_category))

                    # end----------------------------------------------------------------------

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
    # Entry point of the script when executed directly.
    # Calls the interface function to start the application.
    interface()
# --------------------end-----------------------------
