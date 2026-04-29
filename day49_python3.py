text = input()
shift = 3

result = ""

for c in text:
    result += chr(ord(c)+shift)

print(result)
