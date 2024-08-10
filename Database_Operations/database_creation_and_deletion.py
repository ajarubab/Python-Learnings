"""
to make a connection do it in a virtual environment with the steps given below:
0. go inside Database_Operations folder. ( optional )
1. run "python3 -m venv myenv" ------>> it will create "myenv" folder.
2. run "source myenv/bin/activate" (if myenv is made outside Database_operations folder)
2. run "source /Users/rkp/Desktop/Python-Learnings/Database_Operations/myenv/bin/activate" (if myenv is made inside Database_Operations folder)
3. run "pip3 install mysql-connector-python"
4. run your code
5. run "deactivate" when need of virtual environment is finished.
"""

import mysql.connector
from mysql.connector import Error

def check_database_exists(cursor, db_name):
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    for (database,) in databases:
        if database == db_name:
            return True
    return False

try:
    # Establish connection to MySQL
    con = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        passwd=""     # Replace with your MySQL password if required
    )
    
    # Check if the connection was successful
    if con.is_connected():
        print("Connection established successfully")
        
        # Create a cursor object
        mycursor = con.cursor()

        # Define the database name
        db_name = "abdb"

        # Check if the database exists before creation
        if check_database_exists(mycursor, db_name):
            print(f"Database '{db_name}' already exists.")
        else:
            mycursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Database '{db_name}' created successfully.")

        # Check if the database exists before dropping
        if check_database_exists(mycursor, db_name):
            mycursor.execute(f"DROP DATABASE {db_name}")
            print(f"Database '{db_name}' dropped successfully.")
        else:
            print(f"Database '{db_name}' not found, hence deletion not possible.")

except Error as e:
    print(f"Error: {e}")

finally:
    # Ensure the connection is closed
    if con.is_connected():
        con.close()
        print("Connection closed")
