class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(5)
head.next = Node(10)
head.next.next = Node(15)
head.next.next.next = Node(20)

count = 0
current = head

while current:
    count += 1
    current = current.next

print("Length:", count)
