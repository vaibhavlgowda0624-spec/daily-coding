import re

number=input()

if re.fullmatch(r"[6-9]\d{9}",number):
    print("Valid")
else:
    print("Invalid")
