nums = list(map(int, input().split()))
target = int(input())

for i in range(len(nums)):
    if nums[i] == target:
        print("Found at index", i)
        break
else:
    print("Not found")
