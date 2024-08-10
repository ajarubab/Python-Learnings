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

    # Create table with Emp_id as auto-increment primary key and unique constraint on Emp_name and post
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS employeeInfo(
            Emp_id INT AUTO_INCREMENT PRIMARY KEY, 
            Emp_name VARCHAR(100), 
            post VARCHAR(50), 
            salary DECIMAL(10,2),
            UNIQUE (Emp_name, post)
        )
    """)
    print("\n-------- Table created successfully ----------\n")

    # Insert multiple records into the table without specifying Emp_id
    insertdata = "INSERT INTO employeeInfo(Emp_name, post, salary) VALUES (%s, %s, %s)"
    # All the data should be unique otherwise insertion will not take place
    datarecords = [
        ('Amar', 'SQA', 600000),
        ('Prashant', 'Architect', 5000000),
        ('Vihsal', 'Sen Dev', 300000),
        ('Gautam', 'PM', 400000),
        ('Abhay', 'Sen QA', 200000),
    ]

    try:
        mycursor.executemany(insertdata, datarecords)
        con.commit()
        print("----- Record inserted manually into the table is successful. -----\n")
    except mysql.connector.IntegrityError as e:
        print(f"\nError: {e}. Duplicate entry detected, insertion skipped.")

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
    print("\n********** Connection closed ***********\n")
