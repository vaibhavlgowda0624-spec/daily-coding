import random
import string

pwd = ''.join(random.choice(string.ascii_letters) for _ in range(8))

print(pwd)
