from collections import deque

graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["F"],
    "F": []
}

indegree = {node: 0 for node in graph}

for node in graph:
    for neighbour in graph[node]:
        indegree[neighbour] += 1

queue = deque(
    node for node in graph
    if indegree[node] == 0
)

result = []

while queue:
    node = queue.popleft()
    result.append(node)

    for neighbour in graph[node]:
        indegree[neighbour] -= 1

        if indegree[neighbour] == 0:
            queue.append(neighbour)

print(result)
