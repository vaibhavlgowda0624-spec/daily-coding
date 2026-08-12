import json

with open("students.json") as file:
    students = json.load(file)

top_student = max(students, key=lambda x: x["marks"])

print(top_student)
