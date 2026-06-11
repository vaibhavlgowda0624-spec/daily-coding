nums = [1,2,3,2,4]

for n in set(nums):
    if nums.count(n) > 1:
        print(n)
