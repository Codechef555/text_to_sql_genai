import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info = """
CREATE TABLE STUDENT(NAME VARCHAR(50),CLASS VARCHAR(50),
SECTION VARCHAR(50),MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES('Max','Block chain','A',90) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('Riya','Data science','B',85) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('Leo','Data science','A',100) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('George','DEVOPS','A',60) ''')
cursor.execute('''INSERT INTO STUDENT VALUES('Morris','DEVOPS','A',55) ''')

print("The Inserted Records are : ")
data = cursor.execute('''SELECT * FROM STUDENT ''')

for row in data:
    print(row)

## close the connection
    
connection.commit()
connection.close()