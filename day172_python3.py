words = [
    "cat",
    "python",
    "code",
    "web",
    "program"
]

groups = {}

for word in words:
    length = len(word)

    groups.setdefault(length, [])
    groups[length].append(word)

print(groups)
