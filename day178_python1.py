number = int(input("Enter number: "))

total = 0

for i in range(1, number):
    if number % i == 0:
        total += i

if total == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
