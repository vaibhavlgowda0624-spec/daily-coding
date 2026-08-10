import heapq

numbers = [9, 4, 7, 1, 3, 8]

heapq.heapify(numbers)

sorted_numbers = []

while numbers:
    sorted_numbers.append(heapq.heappop(numbers))

print(sorted_numbers)
