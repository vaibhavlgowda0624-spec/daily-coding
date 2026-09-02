a = [1, 2, 3, 4, 5]
b = [2, 3, 5, 7]
c = [2, 5, 8, 9]

common = [
    x for x in a
    if x in b and x in c
]

print("Common Elements:", common)
