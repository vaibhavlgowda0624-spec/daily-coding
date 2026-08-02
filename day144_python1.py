import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE students SET marks=? WHERE name=?",
    (98, "Vaibhav")
)

conn.commit()
conn.close()

print("Record Updated")
