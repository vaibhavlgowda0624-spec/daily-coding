text = input("Enter sentence: ").lower().split()

freq={}

for word in text:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

print(freq)
