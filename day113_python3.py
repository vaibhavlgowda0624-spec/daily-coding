with open("a.txt") as a:
    data=a.read()

with open("copy.txt","w") as b:
    b.write(data)
