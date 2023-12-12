import logging
import azure.functions as func
import mysql.connector
import datetime
import os
import json
from azure.storage.queue import QueueClient
from azure.data.tables import TableServiceClient, TableEntity

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Azure Function Processing a HTTP Request for Attendance Tracking')

    # Retrieve parameters from the request
    student_id = req.params.get('Student_id')
    class_id = req.params.get('Class_id')
    entered_code = req.params.get('input')

    # Check if all required parameters are provided
    if not all([student_id, class_id, entered_code]):
        return func.HttpResponse('{"message": "Missing required parameters: Student_id, Class_id, or code", "status_code": 400}', status_code=400, mimetype="application/json")

    # Database credentials
    host='dockerlab.westeurope.cloudapp.azure.com'
    username='DUDB_1'
    password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ'
    database='DUDB_1'

    # Define the name of the error queue
    error_queue_name = 'dlq' 

    try:
        # Establish database connection
        conn = mysql.connector.connect(
            user=username,
            password=password,
            host=host,
            database=database
        )
        cursor = conn.cursor()

        # New Azure Table Service code
        connection_string = "DefaultEndpointsProtocol=https;AccountName=storagequeues1;AccountKey=FDUPCNSXFsQa9kiKJtmaVBzcNnfjuc8nybvzynfqKK4DRsRwqQ9T+URxhekULKbaHFU+RZ0b9GPi+ASt/bzHvg==;EndpointSuffix=core.windows.net"
        table_service = TableServiceClient.from_connection_string(conn_str=connection_string)
        table_client = table_service.get_table_client(table_name="logtable")

        # Create and log entry
        log_entry = TableEntity()
        log_entry['PartitionKey'] = student_id
        log_entry['RowKey'] = str(datetime.datetime.utcnow())
        log_entry['EnteredCode'] = entered_code

        # Insert the log entry into the table
        table_client.create_entity(entity=log_entry)


        # Validate the entered code against the latest active code in the database
        cursor.execute("SELECT GeneratedCode FROM Codes WHERE Class_id = %s", (class_id))
        reference_code = cursor.fetchone()

        if reference_code and entered_code == reference_code:
            # Update attendance status to 'TRUE' for the student
            cursor.execute("""
                UPDATE Attendance_Records
                SET Present = 1
                WHERE enrollment_id IN (
                    SELECT id
                    FROM Enrollments
                    WHERE Student_id = %d AND Class_id = %d
                );
                """, (student_id, class_id))
            conn.commit()

            return func.HttpResponse('{"message": "Attendance updated to PRESENT."}', mimetype="application/json")

        else:
            # Logging the error attempt in the log-error-attempts queue
            error_attempt = {
                "ReceivedCode": entered_code,
                "Timestamp": str(datetime.datetime.utcnow())
            }
            connection_string = os.environ['AzureWebJobsStorage']
            queue_service = QueueClient.from_connection_string(connection_string, error_queue_name)
            queue_service.send_message(json.dumps(error_attempt))
            return func.HttpResponse('{"message": "Incorrect code entered.", "status_code": 400}', status_code=400, mimetype="application/json")

    except Exception as e:
        logging.error(f"Error: {str(e)}")

        # Logging the error attempt in the log-error-attempts queue
        error_attempt = {
            "ReceivedCode": entered_code,
            "Timestamp": str(datetime.datetime.utcnow())
        }
        connection_string = os.environ['AzureWebJobsStorage']
        queue_service = QueueClient.from_connection_string(connection_string, error_queue_name)
        queue_service.send_message(json.dumps(error_attempt))

        return func.HttpResponse(f'{{"message": "Error: {str(e)}", "status_code": 500}}', status_code=500, mimetype="application/json")
    finally:
        # Close the database connection
        if conn.is_connected():
            conn.close()