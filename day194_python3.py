class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12


employee = Employee("Arun", 35000)

print("Employee:", employee.name)
print("Yearly Salary:", employee.yearly_salary())
