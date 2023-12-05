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
sql_str='''
    INSERT INTO Courses (course_name)
    VALUES
        ('Chemistry'),
        ('Computer Science'),
        ('Physics'),
        ('Biology'),
        ('Mathematics'),
        ('History'),
        ('Art'),
        ('Economics')
    ;
    '''
print(sql_str)
cursor.execute(sql_str)
cnx.commit() # commit is required when you run INSERT statement, to persist new data to tables


#Check to confirm Table COURSES was populated correctly

sql_str='SELECT * FROM Courses;'
print(sql_str)
rs=cursor.execute(sql_str)
rs=cursor.fetchall()
print(rs)



# Populate Table PROFESSORS 
print("=== Inserting a record into Professors")
sql_str='''
    INSERT INTO Professors (first_name, last_name, email, password)
    VALUES
        ('Professor1', 'Lastname1', 'prof1@example.com', 'prof1pass'),
        ('Professor2', 'Lastname2', 'prof2@example.com', 'prof2pass'),
        ('Professor3', 'Lastname3', 'prof3@example.com', 'prof3pass'),
        ('Professor4', 'Lastname4', 'prof4@example.com', 'prof4pass')
    ;
    '''
print(sql_str)
cursor.execute(sql_str)
cnx.commit()

#Check to confirm Table PROFESSORS was populated correctly

sql_str='SELECT * FROM Professors;'
print(sql_str)
rs=cursor.execute(sql_str)
rs=cursor.fetchall()
print(rs)


# Populate Table STUDENTS

print("=== Inserting records into Students")

sql_str='''
    INSERT INTO Students (first_name, last_name, email, password)
    VALUES
        ('John', 'Doe', 'john.doe@example.com', 'password123'),
        ('Jane', 'Smith', 'jane.smith@example.com', 'pass456'),
        ('Bob', 'Johnson', 'bob.johnson@example.com', 'secure789'),
        ('Alice', 'Williams', 'alice.w@example.com', 'alicerules'),
        ('Charlie', 'Brown', 'charlie.b@example.com', 'brown123'),
        ('Eva', 'Miller', 'eva.m@example.com', 'evapass'),
        ('David', 'Wilson', 'david.w@example.com', 'davidpass'),
        ('Grace', 'Hill', 'grace.h@example.com', 'grace123'),
        ('Sam', 'Parker', 'sam.p@example.com', 'sampass'),
        ('Linda', 'Collins', 'linda.c@example.com', 'lindapass')
    ;
    '''
print(sql_str)
cursor.execute(sql_str)
cnx.commit()


#Check to confirm Table STUDENTS was populated correctly

sql_str='SELECT * FROM Students;'
print(sql_str)
rs=cursor.execute(sql_str)
rs=cursor.fetchall()
print(rs)



# Populate Table CLASSES
print("=== Inserting records into Classes")

sql_str='''
    INSERT INTO Classes (class_name, Professor_id, Course_id)
    VALUES
        ('Databases', 1, 2),
        ('Math', 1, 5),
        ('Class3', 1, 6),
        ('Class4', 2, 7),
        ('Class5', 2, 8),
        ('Class6', 2, 4),
        ('Class7', 3, 5),
        ('Class8', 3, 6)
    ;
    '''

print(sql_str)
cursor.execute(sql_str)
cnx.commit()


#Check to confirm Table CLASSES was populated correctly

sql_str='SELECT * FROM Classes;'
print(sql_str)
rs=cursor.execute(sql_str)
rs=cursor.fetchall()
print(rs)



# Populate Table ENROLLMENTS
sql_str3='''
    INSERT INTO Enrollments (Student_id, Class_id)
    VALUES
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 4),
        (10, 2)
    ;
    '''
print(sql_str3)
cursor.execute(sql_str3)

#Check to confirm Table ENROLLMENTS was populated correctly

sql_str='SELECT * FROM Enrollments;'
print(sql_str)
rs=cursor.execute(sql_str)
rs=cursor.fetchall()
print(rs)