nums = list(map(int, input("Enter numbers: ").split()))

duplicates = []

for n in nums:
    if nums.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

print("Duplicates:", duplicates)
