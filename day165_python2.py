matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for column in range(3):
    row = []

    for line in matrix:
        row.append(line[column])

    transpose.append(row)

print(transpose)
