graph = {
    "A": ["B"],
    "B": ["C"],
    "C": ["A"]
}

visited = set()
rec_stack = set()

def has_cycle(node):
    visited.add(node)
    rec_stack.add(node)

    for neighbour in graph[node]:
        if neighbour not in visited:
            if has_cycle(neighbour):
                return True
        elif neighbour in rec_stack:
            return True

    rec_stack.remove(node)
    return False

cycle = False

for node in graph:
    if node not in visited:
        if has_cycle(node):
            cycle = True
            break

print("Cycle Found" if cycle else "No Cycle")
