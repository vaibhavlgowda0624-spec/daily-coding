from dataclasses import dataclass

@dataclass
class Student:
    name: str
    marks: int
    course: str

student = Student("Vaibhav", 92, "MCA")

print(student)
