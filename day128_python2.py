count = 0

with open("sample.txt") as f:
    text = f.read().lower()

for ch in text:
    if ch in "aeiou":
        count += 1

print(count)
