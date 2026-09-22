numbers = [10, 20, 30, 40, 50, 60]

k = int(input("Enter rotation value: "))

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print("Rotated List:", rotated)
