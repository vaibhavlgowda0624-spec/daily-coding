def binary_search(arr, left, right, key):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == key:
        return mid

    if key < arr[mid]:
        return binary_search(arr, left, mid - 1, key)

    return binary_search(arr, mid + 1, right, key)

numbers = [2,4,6,8,10,12]

print(binary_search(numbers, 0, len(numbers)-1, 10))
