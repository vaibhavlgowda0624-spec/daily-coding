nums = list(map(int, input("Enter numbers: ").split())))
k = int(input("Enter rotation count: "))

k = k % len(nums)

rotated = nums[k:] + nums[:k]

print("Rotated list:", rotated)
