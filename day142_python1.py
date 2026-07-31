import sqlite3

conn = sqlite3.connect("students.db")

cursor = conn.cursor()

cursor.execute(
"INSERT INTO students(name,marks) VALUES(?,?)",
("Vaibhav",95)
)

conn.commit()

conn.close()

print("Record Inserted")
