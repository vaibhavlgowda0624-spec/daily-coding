def precedence(operator):
    if operator in "+-":
        return 1

    if operator in "*/":
        return 2

    return 0

def infix_to_postfix(expression):
    stack = []
    result = []

    for char in expression:
        if char.isalnum():
            result.append(char)

        elif char == "(":
            stack.append(char)

        elif char == ")":
            while stack and stack[-1] != "(":
                result.append(stack.pop())

            stack.pop()

        else:
            while (
                stack and
                precedence(stack[-1]) >= precedence(char)
            ):
                result.append(stack.pop())

            stack.append(char)

    while stack:
        result.append(stack.pop())

    return "".join(result)

print(infix_to_postfix("A+B*C"))
