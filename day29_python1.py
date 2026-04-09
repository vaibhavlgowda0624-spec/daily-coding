text = input("Enter text: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:",ch)
        break
else:
    print("No unique character found")
