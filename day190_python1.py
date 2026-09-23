name = input("Enter student name: ")
course = input("Enter course: ")
marks = input("Enter marks: ")

with open("students.txt", "a") as file:
    file.write(name + " | " + course + " | " + marks + "\n")

print("Student record saved successfully.")
