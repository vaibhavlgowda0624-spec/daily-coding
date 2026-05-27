with open("test.txt") as f:
    words = f.read().split()

print(max(words, key=len))
