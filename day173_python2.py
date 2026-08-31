numbers = [0, 1, 0, 3, 12]

non_zero = [
    x for x in numbers
    if x != 0
]

zeros = [
    0 for _ in range(
        len(numbers) - len(non_zero)
    )
]

print(non_zero + zeros)
