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


class Filter_me:
    def __init__(self):
        pass

    @staticmethod
    def sort_all_data(q1):
        """
        Filters data from a table based on specified criteria.
        Parameters:
            q1 (str): Table name.
            q2 (str): Column name.
            query (str): Value to filter by.
        """
        try:
            request = f"SELECT * FROM {q1} "
            read = CRUD()
            read.server_connection()
            data = read.read(request)
            return data
            # print(pd.DataFrame(data))
            # print(f"{q1} filtered successfully")
        except Error as err:
            print(f"Error: '{err}'")
