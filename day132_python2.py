class InvalidAge(Exception):
    pass

age = int(input("Enter age: "))

if age < 18:
    raise InvalidAge("Not eligible")

print("Eligible")
