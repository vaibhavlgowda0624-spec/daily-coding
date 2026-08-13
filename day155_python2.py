graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}

for node, connections in graph.items():
    print(node, "degree =", len(connections))
