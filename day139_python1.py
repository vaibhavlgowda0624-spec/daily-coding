import re

text="Python is powerful."

match=re.search("power",text)

if match:
    print("Found")
