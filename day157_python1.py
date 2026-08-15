import heapq

graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("D", 5)],
    "C": [("B", 1), ("D", 8)],
    "D": []
}

distances = {node: float("inf") for node in graph}
distances["A"] = 0

queue = [(0, "A")]

while queue:
    distance, node = heapq.heappop(queue)

    if distance > distances[node]:
        continue

    for neighbour, weight in graph[node]:
        new_distance = distance + weight

        if new_distance < distances[neighbour]:
            distances[neighbour] = new_distance
            heapq.heappush(queue, (new_distance, neighbour))

print(distances)
