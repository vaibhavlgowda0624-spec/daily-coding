nums = list(map(int, input().split()))

pos = sum(1 for n in nums if n > 0)
neg = sum(1 for n in nums if n < 0)

print("Positive:", pos)
print("Negative:", neg)
