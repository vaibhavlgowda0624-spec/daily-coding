import random,string

pwd = ''.join(random.choices(string.ascii_letters+string.digits,k=8))
print(pwd)
