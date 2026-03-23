numbers = list(map(int, input("Enter numbers seperated by space: ").split()))

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) < 2:
    print("No second largest number")
else:
    print("Second largest:", unique_numbers[-2])
