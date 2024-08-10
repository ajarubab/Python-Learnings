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

try:
    # Establish connection to MySQL
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        # database="rjdb"  # Include this if you want to specify a database
    )
    
    # Check if connection was successful
    if con.is_connected():
        print("Connection established successfully")
        
    # Create a cursor object
    mycursor = con.cursor()
    
except Error as e:
    print(f"Error: {e}")
    
finally:
    # Close the connection if it was opened
    if con.is_connected():
        con.close()
        print("Connection closed")
