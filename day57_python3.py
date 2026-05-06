words = input().split()
print(max((w for w in words if w==w[::-1]), key=len, default="None"))
