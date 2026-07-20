import os

extensions = {}

for file in os.listdir("."):
    if "." in file:
        ext = file.split(".")[-1]
        extensions[ext] = extensions.get(ext, 0) + 1

print(extensions)
