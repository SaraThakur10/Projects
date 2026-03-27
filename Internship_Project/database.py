import sqlite3

DB_NAME = "student_records.db"

def create_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        marks INTEGER,
        attendance INTEGER
    )
    """)

    conn.commit()
    conn.close()