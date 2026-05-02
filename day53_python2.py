text = input()
print([c for c in set(text) if text.count(c)>1])
