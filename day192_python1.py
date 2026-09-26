import json

student = {
    "name": "Rahul",
    "course": "MCA",
    "semester": 3,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data saved.")
