shift = 4

with open("sample.txt") as f:
    text = f.read()

encrypted = ""

for ch in text:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        encrypted += chr((ord(ch)-start+shift)%26+start)
    else:
        encrypted += ch

with open("encrypted.txt","w") as f:
    f.write(encrypted)

print("Encrypted Successfully")
