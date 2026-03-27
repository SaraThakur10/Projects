import pandas as pd
from database import create_connection

# CREATE
def add_student(name, age, marks, attendance):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, marks, attendance) VALUES (?, ?, ?, ?)",
        (name, age, marks, attendance)
    )

    conn.commit()
    conn.close()
    print(f"✅ Student {name} added successfully.")


# READ
def view_students():
    conn = create_connection()

    df = pd.read_sql_query("SELECT * FROM students", conn)
    conn.close()

    if df.empty:
        print("⚠️ No records found.")
    else:
        print(df)


# UPDATE
def update_student(student_id, marks=None, attendance=None):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    record = cursor.fetchone()

    if not record:
        print("❌ Student ID not found.")
        return

    if marks is not None:
        cursor.execute("UPDATE students SET marks=? WHERE id=?", (marks, student_id))

    if attendance is not None:
        cursor.execute("UPDATE students SET attendance=? WHERE id=?", (attendance, student_id))

    conn.commit()
    conn.close()
    print("✅ Student updated successfully.")


# DELETE
def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    if not cursor.fetchone():
        print("❌ Student ID not found.")
        return

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    conn.close()

    print("🗑️ Student deleted successfully.")