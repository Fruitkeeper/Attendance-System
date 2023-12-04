import sqlite3
import mysql.connector

# Creating/Adding Tables
def tables (cxn):
    cursor = cnx.cursor()

    # Create Students table
    create_students='''
    CREATE TABLE IF NOT EXISTS Students (
        id INT  NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(100) ,
        last_name VARCHAR(100) ,
        email VARCHAR(100),
        password VARCHAR(100),
        PRIMARY KEY(id)
    );
    '''
    cursor.execute(create_students)

    # Create Professors table
    create_professors='''
    CREATE TABLE IF NOT EXISTS Professors (
        id INT  NOT NULL AUTO_INCREMENT,
        first_name VARCHAR(100) ,
        last_name VARCHAR(100) ,
        email VARCHAR(100),
        password VARCHAR(100),
        PRIMARY KEY(id)
    );
    '''
    cursor.execute(create_professors)

    # Create Courses table
    create_courses='''
    CREATE TABLE IF NOT EXISTS Courses (
        id INT  NOT NULL AUTO_INCREMENT,
        name VARCHAR(100) ,
        PRIMARY KEY(id)
    );
    '''
    cursor.execute(sql_str3)

    # Create Classes table
    create_classes='''
    CREATE TABLE IF NOT EXISTS Classes (
        id INT  NOT NULL AUTO_INCREMENT,
        class_name VARCHAR(100) ,
        Professor_id INT,
        Student_id INT,
        Course_id INT,
        PRIMARY KEY(id),
        FOREIGN KEY (Professor_id) REFERENCES Professors(id),
        FOREIGN KEY (Student_id) REFERENCES Students(id),
        FOREIGN KEY (Course_id) REFERENCES Courses(id)
    );
    '''
    cursor.execute(create_classes)

    # Create Codes table
    create_codes='''
    CREATE TABLE IF NOT EXISTS Codes (
        id INT  NOT NULL AUTO_INCREMENT,
        Professor_id INT ,
        Class_id INT,
        GeneratedCode VARCHAR(100),
        PRIMARY KEY(id),
        FOREIGN KEY (Professor_id) REFERENCES Professors(id),
        FOREIGN KEY (Class_id) REFERENCES Classes(id)
    );
    '''
    cursor.execute(create_codes)

    # Create Attendance_Records table
    create_records='''
    CREATE TABLE IF NOT EXISTS Attendance_Records (
        record_id INT  NOT NULL AUTO_INCREMENT,
        Student_id INT,
        Class_id INT,
        Present BIT,
        Late BIT,
        Date DATE,
        PRIMARY KEY(record_id),
        FOREIGN KEY (Student_id) REFERENCES Students(id),
        FOREIGN KEY (Class_id) REFERENCES Classes(id)
    );
    '''
    cursor.execute(create_records)

    cxn.commit()


# Populate tables with data
def data (cxn):
    cursor = cnx.cursor()

    # Populate data in students table
    insert_students='''
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
    cursor.execute(insert_students)

    # Populate data in Professors table
    insert_professors='''
    INSERT INTO Professors (first_name, last_name, email, password)
    VALUES
        ('Professor1', 'Lastname1', 'prof1@example.com', 'prof1pass'),
        ('Professor2', 'Lastname2', 'prof2@example.com', 'prof2pass'),
        ('Professor3', 'Lastname3', 'prof3@example.com', 'prof3pass'),
    ;
    '''
    cursor.execute(insert_professors)

    # Populate data in Courses table
    insert_courses='''
    INSERT INTO Courses (name)
    VALUES
        ('Chemistry'),
        ('Computer Science),
        ('Physics'),
        ('Biology'),
        ('Mathematics'),
        ('History'),
        ('Art'),
        ('Economics')
    ;
    '''
    cursor.execute(insert_courses)

    # Populate data in Classes table
    insert_classes='''
    INSERT INTO Classes (class_name, Professor_id, Student_id, Course_id)
    VALUES
        ('Databases', 1, 2, 2),
        ('Math', 1, 3, 5),
        ('Class3', 1, 3, 6),
        ('Class4', 2, 1, 7),
        ('Class5', 2, 2, 8),
        ('Class6', 2, 3, 9),
        ('Class7', 3, 3, 5),
        ('Class8', 3, 1, 6),
    ;
    '''
    cursor.execute(insert_classes)

    # Populate data in Codes table
    print("=== Inserting data into Codes")
    insert_codes='''
    INSERT INTO Codes (GeneratedCode, Professor_id, Class_id)
    VALUES
        ('ABC123', 1, 1),
        ('DEF456', 1, 2),
        ('GHI789', 1, 3),
        ('JKL012', 2, 4),
        ('MNO345', 2, 5),
        ('PQR678', 2, 6),
        ('STU901', 3, 7),
        ('VWX234', 3, 8),
    ;
    '''
    cursor.execute(insert_codes)

    # Populate data in Attendance_Records table
    insert_records='''
    INSERT INTO Attendance_Records (Student_id, Class_id, Present, Late, Date)
    VALUES
        (1, 1, 1, 0, '2023-03-01'),
        (2, 2, 1, 0, '2023-03-01'),
        (3, 3, 0, 0, '2023-03-01'),
        (4, 4, 1, 0, '2023-03-01'),
        (5, 5, 1, 0, '2023-03-01'),
        (6, 6, 0, 0, '2023-03-01'),
        (7, 7, 1, 1, '2023-03-01'),
        (8, 8, 1, 1, '2023-03-01'),
        (9, 9, 1, 0, '2023-03-01'),
        (10, 2, 1, 0, '2023-03-01')
    ;
    '''
    cursor.execute(insert_records)

    cnx.commit()



def main()
    # Connect to MySQL Database

    host='dockerlab.westeurope.cloudapp.azure.com'
    username='DUDB_1'
    password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ'
    database='DUDB_1'

    cnx = mysql.connector.connect(user=username, password=password,
                                    host=host, database=database)

    cursor = cnx.cursor()

    # Testing connection to database
    print("=== Testing connection to the Database")
    sql_str='SELECT now();'
    print(sql_str)
    rs=cursor.execute(sql_str)
    rs=cursor.fetchall()
    print(rs)

    # Class functions to create tables and populate data
    tables(cxn)
    data (cxn)

    # Close Database connection
    cxn.close()

if __name__ = "__main__":
    main()



