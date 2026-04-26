with open("test.txt") as f:
   text = f.read()
   print(sum(1 for c in text if c in "aeiou"))
