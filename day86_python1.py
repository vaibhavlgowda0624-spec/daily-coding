students = ["Rahul", "Ankit", "Vaibhav"]

present = input("Enter present students: ").split()

for s in students:
    if s in present:
        print(s, "Present")
    else:
        print(s, "Absent")
