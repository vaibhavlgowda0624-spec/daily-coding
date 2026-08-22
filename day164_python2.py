text = input("Enter text: ")

stack = list(text)

reverse = ""

while stack:
    reverse += stack.pop()

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
