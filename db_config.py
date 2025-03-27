import psycopg2
import os

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="leave_tracker",
            user="akhilgoyal",
            password=os.getenv("@Goyal03"),  # Use environment variables
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
