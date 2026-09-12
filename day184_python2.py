numbers = [1, 2, 3, 5, 6]

n = 6
result = 0

for i in range(1, n + 1):
    result ^= i

for number in numbers:
    result ^= number

print("Missing Number:", result)
