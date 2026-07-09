text = input()

for ch in set(text):
    if text.count(ch) > 1:
        print(ch, text.count(ch))
