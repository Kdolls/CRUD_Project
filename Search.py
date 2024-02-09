import mysql.connector
from mysql.connector import Error
import pandas as pd


class Search:
    """
    Class handles search operations on different entities.
    """

    def __init__(self):
        self.list_A = ["Students", "Teachers", "Courses", "Enrollments"]

        # keywords
        self.list_student = ["student_id"]
        # Testing feature for the update
        # self.list_student = ["student_id",
        #                      "student_first_name",
        #                      "student_last_name",
        #                      "student_date_of_birth"]

        self.list_teacher = ["teacher_id"]
        # Testing feature for the update
        # self.list_teacher = ["teacher_id",
        #                      "teacher_first_name",
        #                      "teacher_last_name",
        #                      "teacher_date_of_birth",
        #                      "teacher_hire_date"]

        self.list_course = ["course_id"]
        # Testing feature for the update
        # self.list_course = ["course_id",
        #                     "course_name",
        #                     "teacher_id"]

        self.list_enroll = ["enrollment_id"]
        # Testing feature for the update
        # self.list_enroll = ["enrollment_id",
        #                     "student_id",
        #                     "course_id"]

    def menu_A(self):
        """
        Displays the menu for selecting a search category and returns the chosen category.
        """
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

    @staticmethod
    def menu_B(chosen_category, current_list):
        """
        Displays the menu for selecting a keyword from the provided list.
         -chosen_category: The chosen category for search.
         -current_list: The list of keywords for the chosen category.
         The chosen keyword.
        """
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

    @staticmethod
    def menu_C():
        """
        Prompts the user to enter search credentials and returns the input.
        -return: The entered search credentials.
        """
        usr_choice = input("\nEnter credentials: ")
        print('You have chosen:', usr_choice)
        return usr_choice
