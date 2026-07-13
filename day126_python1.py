class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.front = self.rear = -1
        self.size = size

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")
            return

        if self.front == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size

        self.queue[self.rear] = data

    def display(self):
        if self.front == -1:
            print("Queue Empty")
            return

        i = self.front
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.display()
