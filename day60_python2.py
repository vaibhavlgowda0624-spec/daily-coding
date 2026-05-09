pwd = input()

print(len(pwd)>=8 and any(c.isdigit() for c in pwd))
