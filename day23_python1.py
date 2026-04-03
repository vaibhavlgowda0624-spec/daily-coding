num = int(input("Enter number: "))
order = len(str(num))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

if sum == num:
     print("Armstrong Number")
else:
     print("Not Armstrong Number")
