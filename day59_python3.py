nums = list(map(int,input().split()))
print([n for n in set(nums) if nums.count(n)>1])
