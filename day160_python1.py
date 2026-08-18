import random
import string

url = input("Enter URL: ")

code = ''.join(
    random.choices(
        string.ascii_letters + string.digits,
        k=6
    )
)

short_url = "short.ly/" + code

print("Original:", url)
print("Short URL:", short_url)
