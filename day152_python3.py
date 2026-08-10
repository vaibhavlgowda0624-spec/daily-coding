numbers = list(map(float, input().split()))

total = 0

for i, number in enumerate(numbers, start=1):
    total += number
    print("Average:", total / i)
