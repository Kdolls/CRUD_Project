import mysql.connector
from mysql.connector import Error
import pandas as pd


#  connection initialization:
# connection = Classes.CRUD()
# connection.server_connection()


class Search:
    def __init__(self):
        self.list_A = ["Students", "Teachers", "Courses", "Enrollments"]

        # keywords
        self.list_student = ["student_id",
                             "student_first_name",
                             "student_last_name",
                             "student_date_of_birth"]

        self.list_teacher = ["teacher_id",
                             "teacher_first_name",
                             "teacher_last_name",
                             "teacher_date_of_birth",
                             "teacher_hire_date"]

        self.list_course = ["course_id",
                            "course_name",
                            "teacher_id"]

        self.list_enroll = ["enrollment_id",
                            "student_id",
                            "course_id"]

    def menu_A(self):
        for index, lis in enumerate(self.list_A, start=1):
            print(f"{index}. {lis}")
        user_choice = input("\nEnter a number for the Search Category from the above list: ")
        try:
            choice_index = int(user_choice)
            if 1 <= choice_index <= len(self.list_A):
                chosen_category = self.list_A[choice_index - 1]
                print(f"You have chosen: {chosen_category}")
                return chosen_category
            else:
                print("Invalid choice. Please enter a valid number.")
                return None
        except ValueError:
            print("Invalid choice. Please enter a valid number.")
            return None

    def menu_B(self, chosen_category, current_list):
        if current_list:
            for index, keyword in enumerate(current_list, start=1):
                print(f"{index}. {keyword}")

            while True:
                user_choice = input("\nChoose a number from the list: ")
                try:
                    choice_index = int(user_choice)
                    if 1 <= choice_index <= len(current_list):
                        chosen_keyword = current_list[choice_index - 1]
                        print(f"You have chosen: {chosen_keyword}")
                        return chosen_keyword
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid choice. Please enter a valid number.")

    def menu_C(self):
        choice = input("\nEnter credentials: ")
        print('You have chosen:', choice)
        return choice



#
