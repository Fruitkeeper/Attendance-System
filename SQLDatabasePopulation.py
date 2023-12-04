# Attempting to connect to MySQL Database

import mysql.connector

host='dockerlab.westeurope.cloudapp.azure.com'
username='DUDB_1'
password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ'
database='DUDB_1'


cnx = mysql.connector.connect(user=username, password=password,
                                host=host, database=database)

cursor = cnx.cursor()

# Testing connection to database

print("=== Testing connection to the Database")
sql_str = 'SELECT now();'
print(sql_str)
rs = cursor.execute(sql_str)
rs = cursor.fetchall()
print(rs)



# Populate Table COURSES 

print("=== Inserting a record into Courses")
sql_str=f"INSERT INTO Courses(id, name) VALUES ('1', 'Chemistry'),  ('2', 'Computer Science'),  ('3', 'Physics'), ('4', 'Biology'), ('5', 'Discrete Mathematics'), ('6', 'Probability & Statistics');"
print(sql_str)
cursor.execute(sql_str)
cnx.commit() # commit is required when you run INSERT statement, to persist new data to tables


#Check to confirm Table COURSES was populated correctly

sql_str='SELECT * FROM Courses;'
print(sql_str)
rs=cursor.execute(sql_str)
rs=cursor.fetchall()
print(rs)
