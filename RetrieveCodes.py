import logging
import random
import string
import json
import time
import mysql.connector
import azure.functions as func
from azure.functions import HttpRequest, HttpResponse


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    class_id = req.params.get('Class_id')

    try:

        host='dockerlab.westeurope.cloudapp.azure.com'
        username='DUDB_1'
        password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ'
        database='DUDB_1'
        conn = mysql.connector.connect(host=host, user=username, password=password, database=database)
        cursor = conn.cursor()

        cursor.execute("SELECT GeneratedCode FROM Codes WHERE Class_id = %s", (class_id))
        codes = cursor.fetchall()

        
        for code_tuple in codes:
            code = code_tuple[0]  # Extracting the code from the tuple
            logging.info(f"Processing code: {code}")
            time.sleep(10)
            cursor.execute("DELETE FROM Codes WHERE GeneratedCode = %s", (code,))  # Use a tuple or list for parameterized query
            logging.info(f"Deleted code: {code}")
            conn.commit()

        cursor.close()
        conn.close()

        return func.HttpResponse("All codes displayed.", status_code=200)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse("An error occurred while processing the request.", status_code=500)