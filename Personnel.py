import mysql.connector
from mysql.connector import Error
import pandas as pd


# --------------------end-----------------------------

class Members:
    def __init__(self):
        pass

    @staticmethod
    def read_me():
        query = "SELECT * FROM Students"
        return query

    def create_me(self):
        pass
    #
    @staticmethod
    def update_me(self):
        pass

    @staticmethod
    def delete_me():
        pass


