import mysql.connector
from mysql.connector import Error
import pandas as pd
import School_dataset


#   mysql terminal access
#   ====================
#   mysql -u root -p password is password


# SQL server connection
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            db='School'
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


link = create_server_connection('localhost',
                                'root',
                                'password')


# Query execution
def execute(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


# Read database
def read(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")


# data converter into table dataframe formate, adds data to a list
def data_converter(result):
    db = []

    for i in result:
        result = list(result)
        db.append(result)
    return result


# fetch data and present in a list
data = read(link, 'SELECT * FROM Students')

print(pd.DataFrame(data))
