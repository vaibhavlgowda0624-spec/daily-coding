text = input().lower()

count = sum(1 for c in text if c.isalpha() and c not in "aeiou")

print(count)
