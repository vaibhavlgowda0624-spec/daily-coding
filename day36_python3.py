import random, string

pwd = ''.join(random.choice(string.ascii_letters) for _ in range(6))
print(pwd)
