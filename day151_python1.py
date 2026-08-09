class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

def find_min(root):
    while root.left:
        root = root.left
    return root

def delete(root, key):
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)

    elif key > root.key:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        successor = find_min(root.right)
        root.key = successor.key
        root.right = delete(root.right, successor.key)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = None

for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

root = delete(root, 30)

inorder(root)
