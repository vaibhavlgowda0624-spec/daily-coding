class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

a=Node(1)
b=Node(2)

a.next=b

temp=a

while temp:
    print(temp.data)
    temp=temp.next
