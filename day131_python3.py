sentence = input("Enter sentence: ")

words = sentence.split()

lengths = {}

for word in words:
    lengths[len(word)] = lengths.get(len(word), 0) + 1

print(lengths)
