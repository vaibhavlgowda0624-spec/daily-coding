class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(20)
new = Node(10)
new.next = head
head = new

temp = head
while temp:
    print(temp.data)
    temp = temp.next
