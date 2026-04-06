text = input("Enter sentence: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

for ch in alphabet:
    if ch not in text:
        print("Not Pangram")
        break
else:
    print("Pangram")
