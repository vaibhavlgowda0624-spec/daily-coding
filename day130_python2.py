name = input("Name: ")

marks = list(map(int, input("Marks: ").split()))

total = sum(marks)
average = total / len(marks)

print("Student:", name)
print("Total:", total)
print("Average:", average)
