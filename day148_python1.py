from collections import namedtuple

Student = namedtuple("Student",
["name","marks"])

s = Student("Vaibhav",95)

print(s.name)
print(s.marks)
