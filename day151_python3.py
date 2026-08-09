import heapq

numbers = [12, 45, 7, 89, 34, 23, 90]

largest = heapq.nlargest(3, numbers)

print(largest)
