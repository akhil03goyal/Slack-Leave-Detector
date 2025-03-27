import spacy
import psycopg2
from db_config import get_db_connection

# Load trained spaCy model
nlp = spacy.load("output_model")

def store_leave_message(message):
    doc = nlp(message)

    leave_type = None
    leave_date = None

    for ent in doc.ents:
        if ent.label_ == "LEAVE_TYPE":
            leave_type = ent.text
        elif ent.label_ == "DATE":
            leave_date = ent.text

    if not leave_date or not leave_type:
        print("❌ Unable to detect leave type or date. Skipping entry.")
        return

    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO leave_requests (message, leave_date, leave_type) VALUES (%s, %s, %s)",
            (message, leave_date, leave_type)
        )
        conn.commit()
        cursor.close()
        conn.close()
        print(f"✅ Stored: {message} -> Type: {leave_type}, Date: {leave_date}")

# Example message
store_leave_message("I am taking a sick leave tomorrow.")
