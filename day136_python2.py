import json

student = {
    "name": "Vaibhav",
    "marks": 92,
    "course": "MCA"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("JSON file created.")
