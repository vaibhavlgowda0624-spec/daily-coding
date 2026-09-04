import math

number = int(input("Enter number: "))

original = number
total = 0

while number > 0:
    digit = number % 10
    total += math.factorial(digit)
    number //= 10

if total == original:
    print("Strong Number")
else:
    print("Not a Strong Number")
