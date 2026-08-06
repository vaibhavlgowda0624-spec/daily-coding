import os

files = {}

for file in os.listdir("."):
    size = os.path.getsize(file)

    files.setdefault(size, []).append(file)

print(files)
