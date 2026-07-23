from collections import Counter

text = input("Enter sentence: ")

words = text.split()

count = Counter(words)

print(count)
