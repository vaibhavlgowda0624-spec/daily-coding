import string

text = input().lower()
print(set(string.ascii_lowercase) - set(text))
