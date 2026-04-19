import string

text = input()
print(text.translate(str.maketrans('','', string.punctuation)))
