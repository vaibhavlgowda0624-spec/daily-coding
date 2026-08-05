shift = 4

with open("encrypted.txt") as f:
    text = f.read()

decrypted = ""

for ch in text:
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        decrypted += chr((ord(ch)-start-shift)%26+start)
    else:
        decrypted += ch

print(decrypted)
