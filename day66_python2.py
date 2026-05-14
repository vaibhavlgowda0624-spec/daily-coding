text = input("Enter text: ")
shift = 2

encrypted = ""

for ch in text:
    encrypted += chr(ord(ch) + shift)

print("Encrypted:", encrypted)
