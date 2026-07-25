import json

with open("student.json") as file:
    data=json.load(file)

print(data)
