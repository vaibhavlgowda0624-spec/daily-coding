count=0

with open("sample.txt") as f:
    for line in f:
        if line.strip()=="":
            count+=1

print(count)
