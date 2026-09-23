try:
    with open("students.txt", "r") as file:
        records = file.readlines()

    print("Student Records:")

    for record in records:
        print(record.strip())

except FileNotFoundError:
    print("No student records found.")
