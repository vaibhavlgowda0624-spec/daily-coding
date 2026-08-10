import heapq

queue = []

heapq.heappush(queue, (2, "Normal Task"))
heapq.heappush(queue, (1, "Urgent Task"))
heapq.heappush(queue, (3, "Low Priority"))

while queue:
    priority, task = heapq.heappop(queue)
    print(priority, task)
