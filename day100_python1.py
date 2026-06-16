students = {}

name = input("Name: ")
marks = int(input("Marks: "))

students[name] = marks

for k,v in students.items():
    print(k,v)
