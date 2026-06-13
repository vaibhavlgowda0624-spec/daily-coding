text = input().lower()

v = sum(c in "aeiou" for c in text)
c = sum(ch.isalpha() and ch not in "aeiou" for ch in text)

print(v,c)
