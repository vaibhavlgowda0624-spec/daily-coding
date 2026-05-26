text = input()

digits = sum(c.isdigit() for c in text)
letters = sum(c.isalpha() for c in text)
spaces = sum(c.isspace() for c in text)

print(digits, letters, spaces)
