numbers = [12, 7, 9, 20, 34, 15, 8, 3]

groups = {
    "Even": [],
    "Odd": []
}

for number in numbers:
    if number % 2 == 0:
        groups["Even"].append(number)
    else:
        groups["Odd"].append(number)

print(groups)
