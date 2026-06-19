with open("test.txt") as f:
    lines = f.readlines()

for line in lines:
    if line.strip():
        print(line.strip())
