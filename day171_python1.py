def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]

    smaller = [
        x for x in numbers[1:]
        if x <= pivot
    ]

    larger = [
        x for x in numbers[1:]
        if x > pivot
    ]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


numbers = [8, 3, 1, 7, 0, 10, 2]

print(quick_sort(numbers))
