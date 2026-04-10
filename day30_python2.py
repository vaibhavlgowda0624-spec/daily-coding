nums = list(map(int, input("Enter numbers: ").split()))

if nums == sorted(nums):
   print("List is sorted")
else:
   print("List is not sorted")
