from collections import deque

queue = deque()

queue.append("Student 1")
queue.append("Student 2")
queue.append("Student 3")

while queue:
    print("Serving:", queue.popleft())
