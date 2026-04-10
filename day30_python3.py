nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

found = False

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
           print("Pair found:", nums[i], nums[j])
           found = True

if not found:
    print("No pair found")
