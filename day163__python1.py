def is_balanced(expression):
    stack = []

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in expression:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0

expression = input("Enter expression: ")

print(
    "Balanced"
    if is_balanced(expression)
    else "Not Balanced"
)
