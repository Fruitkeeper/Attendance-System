import logging
import random
import string
import json
import time
import mysql.connector
import azure.functions as func
from azure.functions import HttpRequest, HttpResponse

def generate_random_code(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def main(req: HttpRequest) -> HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    host='dockerlab.westeurope.cloudapp.azure.com'
    username='DUDB_1'
    password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ'
    database='DUDB_1'

    try:
        conn = mysql.connector.connect(host=host, user=username, password=password, database=database)
        cursor = conn.cursor()
        
        # Generate 10 random codes
        codes = [generate_random_code() for _ in range(10)]

        # Connect to the database and insert the codes
        for code in codes:
            cursor.execute("INSERT INTO Codes (GeneratedCode) VALUES (%s)", (code,))
        conn.commit()
        conn.close()

        return func.HttpResponse("10 random codes generated and added to the database.", status_code=200)
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse("An error occurred while processing the request.", status_code=500)
