text = input("Enter text: ")
shift = 3

result = ""

for ch in text:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        result += chr((ord(ch) - start + shift) % 26 + start)
    else:
        result += ch

print("Encrypted:", result)
