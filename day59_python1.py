words = input().split()
print(sum(1 for w in words if len(w)%2==0))
