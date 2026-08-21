class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()

        return None

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
