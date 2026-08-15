def subsets(numbers):
    result = []

    def backtrack(index, current):
        if index == len(numbers):
            result.append(current.copy())
            return

        backtrack(index + 1, current)

        current.append(numbers[index])
        backtrack(index + 1, current)
        current.pop()

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))
