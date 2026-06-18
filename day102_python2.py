text = input().split()

count = sum(1 for word in text if word[0].isupper())

print(count)
