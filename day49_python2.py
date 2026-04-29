import string

text = input()
missing = set(string.ascii_lowercase) - set(text)
print(missing)
