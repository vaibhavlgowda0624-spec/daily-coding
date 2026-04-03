nums = list(map(int, input("Enter numbers seperated by space: ").split()))

nums = list(set(nums))
nums.sort()      #remove duplicates

print("Second Largest:", nums[-2])
