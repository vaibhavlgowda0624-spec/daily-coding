nums = [1,-2,3,4,-1]

max_sum = current = nums[0]

for n in nums[1:]:
    current = max(n, current+n)
    max_sum = max(max_sum, current)

print(max_sum)
