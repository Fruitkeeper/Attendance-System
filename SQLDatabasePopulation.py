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

