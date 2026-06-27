words=input().split()

for w in words:
    if w==w[::-1]:
        print(w)
