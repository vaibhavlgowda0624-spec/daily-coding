list1 = list(map(int, input("enter first list: ").split()))
list2 = list(map(int, input("enter second list: ").split()))

common = []

for i in list1:
    if i in list2 and i not in common:
         common.append(i)
print("Common elements:", common)
