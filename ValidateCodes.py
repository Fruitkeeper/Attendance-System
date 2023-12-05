import azure.functions as func
import mysql.connector

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Assuming the submitted code is sent in the request body as JSON

    if req.method == 'GET':
        submitted_code = req.params.get('submittedCode')
    elif req.method == 'POST':
        req_body = req.get_body().decode('utf-8')
        submitted_code = req_body.strip() if req_body else None

    try:

        submitted_code = req_body.strip()

        if not submitted_code:
            return func.HttpResponse(
                "Please provide a submitted code.",
                status_code=400
            )

        # Connect to your MySQL database
        conn = mysql.connector.connect(
            host='dockerlab.westeurope.cloudapp.azure.com',
            user='DUDB_1',
            password='4A0z062O97mYrF41wqSs2pXX_crGHuxIEy9Z7g-ogPQ',
            database='DUDB_1',
        )

        cursor = conn.cursor()

        # Fetch the reference code from the database
        cursor.execute("SELECT GeneratedCode FROM Codes WHERE class_id = %s", (123,))
        row = cursor.fetchone()
        reference_code = row[0] if row else None

        if reference_code is None:
            return func.HttpResponse(
                "Reference code not found in the database.",
                status_code=404
            )

        # Compare the submitted code with the reference code from the database
        codes_match = (submitted_code == reference_code)

        if codes_match:
            return func.HttpResponse(
                f"Codes match. Submission accepted.",
                status_code=200
            )
        else:
            return func.HttpResponse(
                f"Codes do not match. Submission rejected.",
                status_code=403
            )

    except mysql.connector.Error as e:
        return func.HttpResponse(
            f"Error connecting to MySQL: {e}",
            status_code=500
        )

    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
