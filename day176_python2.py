start = int(input("Enter start: "))
end = int(input("Enter end: "))

for number in range(start, end + 1):

    if number < 2:
        continue

    prime = True

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break

    if prime:
        print(number, end=" ")
