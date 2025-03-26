import psycopg2
from database import get_db_connection

def fetch_leave_requests():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM leave_requests ORDER BY detected_on DESC")
        results = cursor.fetchall()

        for row in results:
            print(f"ID: {row[0]}, Message: {row[1]}, Date: {row[2]}, Type: {row[3]}, Detected On: {row[4]}")

        cursor.close()
        conn.close()

# Fetch and display stored leave messages
fetch_leave_requests()
