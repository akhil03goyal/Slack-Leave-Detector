import psycopg2
from db_config import get_db_connection  # Fixed incorrect import

def fetch_leave_requests():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, message, leave_date, leave_type, detected_on FROM leave_requests ORDER BY detected_on DESC")
        results = cursor.fetchall()

        for row in results:
            print(f"ID: {row[0]} | Message: {row[1]} | Date: {row[2]} | Type: {row[3]} | Detected On: {row[4]}")

        cursor.close()
        conn.close()

# Fetch and display stored leave messages
fetch_leave_requests()
