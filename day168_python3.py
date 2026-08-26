def list_sum(numbers, index=0):

    if index == len(numbers):
        return 0

    return numbers[index] + list_sum(numbers, index + 1)

numbers = [10, 20, 30, 40]

print("Sum:", list_sum(numbers))
