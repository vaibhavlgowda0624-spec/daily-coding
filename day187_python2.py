class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)


student = Student("Arun", [78, 85, 91, 88])

print("Student:", student.name)
print("Average:", student.average())
