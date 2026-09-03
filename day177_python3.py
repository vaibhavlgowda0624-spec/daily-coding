number = int(input("Enter number: "))

product = 1

while number > 0:
    product *= number % 10
    number //= 10

print("Product of Digits:", product)
