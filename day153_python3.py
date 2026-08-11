numbers = [4, 2, 8, 1, 9, 3]

maximum = numbers[0]

for number in numbers:
    maximum = max(maximum, number)
    print(maximum)
