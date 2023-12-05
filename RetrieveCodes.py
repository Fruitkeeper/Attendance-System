import logging
import random
import string
import json
import time
import mysql.connector
import azure.functions as func
from azure.functions import HttpRequest, HttpResponse


@app.route(route="http_trigger2", auth_level=func.AuthLevel.ANONYMOUS)
def http_trigger2(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:

        host='dockerlab.westeurope.cloudapp.azure.com',
        username='DUDB_1',
        password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ',
        database='DUDB_1',
        conn = mysql.connector.connect(
                    host=host,
                    user=username,
                    password=password,
                    database=database
                )
        cursor = conn.cursor()

        cursor.execute("SELECT GeneratedCode FROM Codes")
        codes = cursor.fetchall()
        
        for code in codes:
            # Here, you can replace this print statement with your logic to display the code on your webpage.
            print(code[0])
            time.sleep(30)  # Wait for 30 seconds before displaying the next code

        cursor.close()
        conn.close()

        return func.HttpResponse("All codes displayed.", status_code=200)

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return func.HttpResponse("An error occurred while processing the request.", status_code=500)
