import string

text=input()

count=sum(c in string.punctuation for c in text)

print(count)
