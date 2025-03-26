import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="leave_tracker",
            user="/////",
            password="/////",
            host="localhost",
            port="5432"  # Change if using a different port
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
