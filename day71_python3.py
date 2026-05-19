with open("a.txt") as a:
    content = a.read()

with open("b.txt","w") as b:
    b.write(content)
