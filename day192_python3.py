import json

with open("student.json", "r") as file:
    student = json.load(file)

student["marks"] = 92

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Marks updated successfully.")
