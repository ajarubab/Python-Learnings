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
    # Connect to the database
    con = mysql.connector.connect(host="localhost", user="root", passwd="", database="rjdb")

    if con.is_connected():
        print("\n\n******** Connection established. *********")

    # Create a cursor object
    mycursor = con.cursor()

    # Fetch and display the data from the table
    mycursor.execute("SELECT * FROM employeeInfo")
    rows = mycursor.fetchall()  # Fetch all rows

    print("\n---------- Data in the table employeeInfo: ----------\n\n")
    for row in rows:
        print(row)

    # Prompt user for the name to delete
    emp_name = input("\nEnter the employee name to delete: ")

    # Check if the record exists
    mycursor.execute("SELECT COUNT(*) FROM employeeInfo WHERE Emp_name=%s", (emp_name,))
    count = mycursor.fetchone()[0]  # Fetch the count of rows

    if count > 0:
        # If the record is found, perform the delete
        mycursor.execute("DELETE FROM employeeInfo WHERE Emp_name=%s", (emp_name,))
        con.commit()
        print("\nData removed successfully.")

        # Fetch and display the data from the table
        mycursor.execute("SELECT * FROM employeeInfo")
        rows = mycursor.fetchall()  # Fetch all rows

        print("\n---------- Data remaining in the table employeeInfo: ----------\n\n")
        for row in rows:
            print(row)
    else:
        # If the record is not found, display a message
        print("\n\nDeletion not possible as data not found in table.")

except Error as e:
    print(f"Error: {e}")
    con.rollback()

finally:
    if con.is_connected():
        con.close()
        print("\n\n********** Connection closed ***********\n")