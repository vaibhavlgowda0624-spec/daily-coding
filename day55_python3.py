d1 = {"a":1}
d2 = {"a":2,"b":3}

for k,v in d2.items():
    d1[k] = d1.get(k,0) + v

print(d1)
