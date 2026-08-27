def binary_search(numbers, target, left, right):

    if left > right:
        return -1

    middle = (left + right) // 2

    if numbers[middle] == target:
        return middle

    if target < numbers[middle]:
        return binary_search(
            numbers, target, left, middle - 1
        )

    return binary_search(
        numbers, target, middle + 1, right
    )

numbers = [10, 20, 30, 40, 50]

target = 40

result = binary_search(
    numbers,
    target,
    0,
    len(numbers) - 1
)

print("Index:", result)
