text = input()
words = text.split()

emails = [w for w in words if "@" in w]
print(emails)
