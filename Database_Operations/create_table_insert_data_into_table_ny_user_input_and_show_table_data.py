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
    con = mysql.connector.connect(host="localhost", user="root", passwd="", database="rjdb")

    # Check if the connection was successful
    if con.is_connected():
        print("\n\n******** Connection established successfully *********")

    
    # Create a cursor object
    mycursor = con.cursor()

    # Create a table
    mycursor.execute("CREATE TABLE IF NOT EXISTS employeeInfo(Emp_id int, Emp_name varchar(100), post varchar(50), salary decimal(10,2))")
    print("\n\n-------- Table created successfully ----------\n")

    # Collect user input
    getId = int(input("Enter employee Id :\t"))
    getName = input("Enter employee Name :\t")
    getPost = input("Enter employee Designation :\t")
    getSal = int(input("Enter employee salary :\t"))

    # Insert the data based on user input
    insertdata = "INSERT INTO employeeInfo (Emp_id, Emp_name, post, salary) VALUES (%s, %s, %s, %s)"
    datarecord = (getId, getName, getPost, getSal)

    mycursor.execute(insertdata, datarecord)
    con.commit()
    print("----- Record inserted sucessfully into the table. -----\n")
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
