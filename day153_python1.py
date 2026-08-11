from collections import deque

items = deque([10, 20, 30])

items.appendleft(5)
items.append(40)

print(items)

items.pop()
items.popleft()

print(items)
