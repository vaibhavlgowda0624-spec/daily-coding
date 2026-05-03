import string

text = input()
print(sum(1 for c in text if c in string.punctuation))
