numbers = [100, 4, 200, 1, 3, 2]

number_set = set(numbers)
longest = 0

for number in number_set:
    if number - 1 not in number_set:
        current = number
        length = 1

        while current + 1 in number_set:
            current += 1
            length += 1

        longest = max(longest, length)

print("Longest Consecutive Sequence:", longest)
