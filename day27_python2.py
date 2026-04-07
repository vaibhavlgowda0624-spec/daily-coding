list1 = list(map(int, input("Enter sorted list1: ").split()))
list2 = list(map(int, input("Enter sorted list2: ").split()))

merged = sorted(list1 + list2)

print("Merged list:", merged)
