A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(2):
    row = []

    for j in range(2):
        row.append(A[i][j] + B[i][j])

    result.append(row)

print(result)
