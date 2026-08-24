class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(25)
head.next.next = Node(40)

target = int(input("Enter value: "))

current = head
found = False

while current:
    if current.data == target:
        found = True
        break
    current = current.next

print("Found" if found else "Not Found")
