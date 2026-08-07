import os

count = {}

for file in os.listdir("."):
    ext = os.path.splitext(file)[1]

    count[ext] = count.get(ext,0)+1

print(count)
