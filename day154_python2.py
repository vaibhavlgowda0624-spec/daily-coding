import json

students = [
    {"name": "Vaibhav", "marks": 90},
    {"name": "Rahul", "marks": 85}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

print("Data saved")
