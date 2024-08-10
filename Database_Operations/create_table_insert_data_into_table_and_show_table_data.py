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
        user="root",  # Replace with your MySQL username
        passwd="",    # Replace with your MySQL password if required
        database="rjdb"
    )

    # Check if the connection was successful
    if con.is_connected():
        print("\n\n******** Connection established successfully *********")
    
    # Create a cursor object
    mycursor = con.cursor()

    # Create a table
    mycursor.execute("CREATE TABLE IF NOT EXISTS employeeInfo (Emp_id INT, Emp_name VARCHAR(100), post VARCHAR(50), salary DECIMAL(10,2))")
    print("\n\n-------- Table created successfully ----------\n")

    # Insert a record into the table
    mycursor.execute("INSERT INTO employeeInfo (Emp_id, Emp_name, post, salary) VALUES (102, 'Raja', 'SDE2', 100000)")
    con.commit()
    print("----- Record inserted manually into the table is successful. -----\n")

    # Show all tables in the database
    print("----- List of all tables of this database -----\n")
    mycursor.execute("SHOW TABLES")
    for table in mycursor:
        print(table)

    # Fetch and display the data from the table
    mycursor.execute("SELECT * FROM employeeInfo")
    rows = mycursor.fetchall()  # Fetch all the rows

    print("\n---------- Data in the table employeeInfo: ----------\n\n")
    for row in rows:
        print(row)

except Error as e:
    print(f"Error: {e}")
    con.rollback()
finally:
    con.close()
    print("\n\n********** Connection closed ***********\n")
