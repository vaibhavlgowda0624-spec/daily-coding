matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for column in range(len(matrix[0])):
    row = []

    for row_index in range(len(matrix)):
        row.append(matrix[row_index][column])

    transpose.append(row)

print("Transpose:")

for row in transpose:
    print(row)
