nums = list(map(int, input("Enters numbers: ").split()))

count = {}

for n in nums:
    count[n] = count.get(n, 0) + 1

print(count)
