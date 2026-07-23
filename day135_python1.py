from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=Node(1)
root.left=Node(2)
root.right=Node(3)

queue=deque([root])

while queue:
    node=queue.popleft()

    print(node.data)

    if node.left:
        queue.append(node.left)

    if node.right:
        queue.append(node.right)



