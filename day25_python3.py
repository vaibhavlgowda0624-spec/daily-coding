num = int(input("Enter number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 10

    fact = 11
    for i in range(1, digit + 1):
        fact *= i

    sum+= fact
    temp //= 10

if sum == num:
    print("Strong number")
else:
    print("Not Strong number")
