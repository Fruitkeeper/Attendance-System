import mysql.connector

host='dockerlab.westeurope.cloudapp.azure.com'
username='DUDB_1'
password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ'
database='DUDB_1'


cnx = mysql.connector.connect(user=username, password=password,
                                host=host, database=database)

cursor = cnx.cursor()