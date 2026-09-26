import json

with open("student.json", "r") as file:
    student = json.load(file)

print("Name:", student["name"])
print("Course:", student["course"])
print("Semester:", student["semester"])
print("Marks:", student["marks"])
