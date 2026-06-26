text=input()

print("".join(c for c in text if not c.isdigit()))
