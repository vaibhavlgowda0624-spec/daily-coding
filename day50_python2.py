words = input().split()
print([w for w in words if w == w[::-1]])
