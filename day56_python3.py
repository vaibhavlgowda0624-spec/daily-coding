words = input().split()
print(sum(1 for w in words if w[0].lower() in "aeiou"))
