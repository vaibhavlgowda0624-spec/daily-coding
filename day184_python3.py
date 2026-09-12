password = input("Enter password: ")

has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)

if len(password) >= 8 and has_digit and has_upper and has_lower:
    print("Strong Password")
elif len(password) >= 6:
    print("Medium Password")
else:
    print("Weak Password")
