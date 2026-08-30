numbers = [1, 2, 3, 4, 5]

positions = int(input("Rotate by: "))

positions %= len(numbers)

rotated = (
    numbers[-positions:] +
    numbers[:-positions]
)

print(rotated)
