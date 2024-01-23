import mysql.connector
from mysql.connector import Error
import pandas as pd
import School_dataset


#   mysql terminal access
#   ====================
#   mysql -u root -p {for initiating my sql} password == password


# SQL server connection function
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


link = create_server_connection('localhost', 'root', 'password')


# Query execution function
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")


#   table creation
# execute_query(link, students_table)
# execute_query(link, teachers_table)
# execute_query(link, courses_table)
# execute_query(link, enrollments_table)

#   student sample values
# execute_query(link,students_values)
# execute_query(link,teachers_values)
# execute_query(link,courses_values)
# execute_query(link,enrollment_values)

execute_query(link, 'SHOW TABLES')
