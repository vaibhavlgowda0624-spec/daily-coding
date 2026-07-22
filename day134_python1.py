class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

root=Node(10)
root.left=Node(5)
root.right=Node(20)

def height(node):
    if node is None:
        return 0

    return 1 + max(height(node.left), height(node.right))

print(height(root))
