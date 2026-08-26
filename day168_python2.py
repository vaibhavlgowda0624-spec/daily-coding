numbers = [15, 28, 42, 67, 89]

target = int(input("Enter number: "))

for index, value in enumerate(numbers):

    if value == target:
        print("Found at index:", index)
        break
else:
    print("Not Found")
