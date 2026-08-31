number = int(input("Enter number: "))

digits = str(number)
power = len(digits)

total = sum(
    int(digit) ** power
    for digit in digits
)

if total == number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
