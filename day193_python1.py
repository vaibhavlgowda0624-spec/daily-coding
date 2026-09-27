import csv

students = [
    ["Name", "Course", "Marks"],
    ["Rahul", "MCA", 85],
    ["Arun", "MCA", 91],
    ["Kiran", "MCA", 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("CSV file created.")
