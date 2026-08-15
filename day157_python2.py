from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str
    salary: int

employee = Employee(
    "Rahul",
    "IT",
    50000
)

print(employee.name)
print(employee.department)
print(employee.salary)
