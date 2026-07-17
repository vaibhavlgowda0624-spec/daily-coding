text = input()

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

for k, v in freq.items():
    print(k, ":", v)
