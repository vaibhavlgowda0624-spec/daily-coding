numbers = [2, 1, 5, 3, 4, 7, 6]
window = 3

for i in range(len(numbers) - window + 1):
    current = numbers[i:i + window]
    print(max(current))
