marks = {
    "Rahul": 85,
    "Arun": 92,
    "Kiran": 78,
    "Vijay": 88
}

sorted_marks = sorted(
    marks.items(),
    key=lambda item: item[1],
    reverse=True
)

for name, mark in sorted_marks:
    print(name, ":", mark)
