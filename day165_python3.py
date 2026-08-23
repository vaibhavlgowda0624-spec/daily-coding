matrix = [
    [5, 2, 3],
    [4, 8, 6],
    [7, 1, 9]
]

main_diagonal = 0
secondary_diagonal = 0

n = len(matrix)

for i in range(n):
    main_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][n - i - 1]

print("Main:", main_diagonal)
print("Secondary:", secondary_diagonal)
