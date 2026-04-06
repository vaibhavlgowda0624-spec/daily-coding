list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

intersection = [x for x in list1 if x in list2]

print("Intersection:", intersection)
