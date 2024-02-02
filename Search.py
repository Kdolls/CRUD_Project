import mysql.connector
from mysql.connector import Error
import pandas as pd
# import Classes



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

        # Display the choice menu
    def menu_A(self):
        print("Choose search category: \n")
        for index, lis in enumerate(self.list_A, start=1):
            print(f"{index}. {lis}")
        # Get user input
        user_choice = input("\n Enter the number of your choice:  ")
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

    def menu_B(self):
        # print("Choose search keyword:\n")
        current_list = None
        # Determine the current list based on the chosen category from menu_A
        chosen_category = self.menu_A()
        if chosen_category == "Students":
            current_list = self.list_student
        elif chosen_category == "Teachers":
            current_list = self.list_teacher
        elif chosen_category == "Courses":
            current_list = self.list_course
        elif chosen_category == "Enrollments":
            current_list = self.list_enroll

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
        # Get user input
        choice = str(input("\nEnter credentials:  "))
        print('you have chosen: ', choice)

        return choice


# if __name__ == "__main__":
#
#     StudentDatabase.filter_data(menu_A(), menu_B(), menu_C())

# test = Search()
# test.menu_A()
# test.menu_B()
# test.menu_C()
#
