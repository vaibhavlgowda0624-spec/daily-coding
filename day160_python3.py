def count_paths(rows, cols):
    if rows == 1 or cols == 1:
        return 1

    return (
        count_paths(rows - 1, cols)
        + count_paths(rows, cols - 1)
    )

print("Paths:", count_paths(3, 3))
