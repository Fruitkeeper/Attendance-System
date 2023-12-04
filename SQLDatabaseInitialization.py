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


# Creating/Adding Tables to MySQL Database

# Students Table
sql_str1='''CREATE TABLE IF NOT EXISTS Students (
    id INT  NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) ,
    last_name VARCHAR(100) ,
    email VARCHAR(100),
    password VARCHAR(100),
    PRIMARY KEY(id)
);'''
print(sql_str1)
cursor.execute(sql_str1)


# Professors Table
sql_str2='''CREATE TABLE IF NOT EXISTS Professors (
    id INT  NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(100) ,
    last_name VARCHAR(100) ,
    email VARCHAR(100),
    password VARCHAR(100),
    PRIMARY KEY(id)
);'''
print(sql_str2)
cursor.execute(sql_str2)

# Courses Table
sql_str3='''CREATE TABLE IF NOT EXISTS Courses (
    id INT  NOT NULL AUTO_INCREMENT,
    course_name VARCHAR(100) ,
    PRIMARY KEY(id)
);'''
print(sql_str3)
cursor.execute(sql_str3)


# Classes Table
sql_str4='''CREATE TABLE IF NOT EXISTS Classes (
    id INT  NOT NULL AUTO_INCREMENT,
    class_name VARCHAR(100) ,
    Professor_id INT,
    Course_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY (Professor_id) REFERENCES Professors(id),
    FOREIGN KEY (Course_id) REFERENCES Courses(id)
);'''
print(sql_str4)
cursor.execute(sql_str4)

# Codes Table
sql_str5='''CREATE TABLE IF NOT EXISTS Codes (
    id INT  NOT NULL AUTO_INCREMENT,
    Class_id INT,
    GeneratedCode VARCHAR(100),
    PRIMARY KEY(id),
    FOREIGN KEY (Class_id) REFERENCES Classes(id)
);'''
print(sql_str5)
cursor.execute(sql_str5)



# Enrollments Table
sql_str6='''CREATE TABLE IF NOT EXISTS Enrollments (
    id INT  NOT NULL AUTO_INCREMENT,
    Student_id INT,
    Class_id INT,
    PRIMARY KEY(id),
    FOREIGN KEY (Student_id) REFERENCES Students(id),
    FOREIGN KEY (Class_id) REFERENCES Classes(id)
);'''
print(sql_str6)
cursor.execute(sql_str6)



# Attendance_Records Table
sql_str7='''CREATE TABLE IF NOT EXISTS Attendance_Records (
    id INT NOT NULL AUTO_INCREMENT,
    enrollment_id INT,
    Present BIT,
    Late BIT,
    Date DATE,
    PRIMARY KEY(id),
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments(id)
);'''
print(sql_str7)
cursor.execute(sql_str7)


# Attempt to show all table names in MySQL Database to confirm tables were created successfully

sql_str='show tables;'
rs=cursor.execute(sql_str)
rs=cursor.fetchall()
print(rs)


# Populate Table COURSES as data in this table is fixed from start

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




