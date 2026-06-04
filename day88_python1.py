text = input("Text: ")

encrypted = ""

for ch in text:
    encrypted += chr(ord(ch) + 1)

print(encrypted)
