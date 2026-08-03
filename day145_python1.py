import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(
    "DELETE FROM students WHERE name=?",
    ("Vaibhav",)
)

conn.commit()
conn.close()

print("Record Deleted")
