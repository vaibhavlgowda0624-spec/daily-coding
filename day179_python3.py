text = input("Enter string: ")
positions = int(input("Rotate by: "))

positions %= len(text)

result = (
    text[-positions:] +
    text[:-positions]
)

print("Rotated String:", result)
