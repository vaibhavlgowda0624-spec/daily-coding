text = input()

for ch in set(text):
    print(ch, ":", text.count(ch))
