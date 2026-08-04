class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def min_value(node):
    current = node
    while current.left:
        current = current.left
    return current.key

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)

print("Minimum:", min_value(root))
