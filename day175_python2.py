numbers = [
    -2, 1, -3, 4,
    -1, 2, 1, -5, 4
]

current = numbers[0]
maximum = numbers[0]

for number in numbers[1:]:

    current = max(
        number,
        current + number
    )

    maximum = max(
        maximum,
        current
    )

print("Maximum Sum:", maximum)
