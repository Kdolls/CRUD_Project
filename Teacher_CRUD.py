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
                print("1. Create Teacher")
                print("2. Read Teachers")
                print("3. Update Teacher")
                print("4. Delete Teacher")
                print("5. Return\n")

                choice = input("Enter your choice (1-5): ")

                if choice == '1':
                    teacher_id = input("Enter teacher ID: ")
                    first_name = input("Enter first name: ")
                    last_name = input("Enter last name: ")
                    date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                    hire_date = input("Enter hire date (YYYY-MM-DD): ")
                    Database.create_teacher(teacher_id, first_name, last_name, date_of_birth, hire_date)

                elif choice == '2':
                    Database.read_all_teachers()

                elif choice == '3':
                    teacher_id = input("Enter teacher ID to update: ")
                    new_first_name = input("Enter new first name: ")
                    new_last_name = input("Enter new last name: ")
                    new_date_of_birth = input("Enter new date of birth in form of (YYYY-MM-DD): ")
                    new_hire_date = input("Enter new hire date in form of (YYYY-MM-DD): ")
                    Database.update_teacher(teacher_id, new_first_name, new_last_name,
                                            new_date_of_birth, new_hire_date)

                elif choice == '4':
                    teacher_id = input("Enter teacher ID to delete: ")
                    Database.delete_teacher(teacher_id)

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


