s = input()
stack = []

for c in s:
    if c == "(":
        stack.append(c)
    elif c == ")":
        if not stack:
            print("Unbalanced")
            break
        stack.pop()
else:
    print("Balanced" if not stack else "Unbalanced")
