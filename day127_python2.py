count = 0

with open("sample.txt") as f:
    data = f.read()

for ch in data:
    if ch.isdigit():
        count += 1

print("Digits:", count)
