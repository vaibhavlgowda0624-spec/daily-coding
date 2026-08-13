graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

stack = ["A"]
visited = set()

while stack:
    node = stack.pop()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in reversed(graph[node]):
            stack.append(neighbour)
