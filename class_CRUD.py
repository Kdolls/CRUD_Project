import mysql.connector
from mysql.connector import Error
import pandas as pd
import School_dataset



class CRUD:
    def __init__(self):
        self.connection = None

    def server_connection(self, host_name, user_name, user_password, db_name='School'):
        try:
            self.connection = mysql.connector.connect(
                host=host_name,
                user=user_name,
                passwd=user_password,
                db=db_name
            )
            print("Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")

    def execute(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query successful")
        except Error as err:
            print(f"Error: '{err}'")

    def read(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as err:
            print(f"Error: '{err}'")

    # def data_converter(self, result):
    #     db = []
    #     for row in result:
    #         db.append(list(row))
    #     return db


read_db = CRUD()
read_db.server_connection('localhost', 'root', 'password')
data = read_db.read('SELECT * FROM Teachers')
print(pd.DataFrame(data))
