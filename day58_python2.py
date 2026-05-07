nums = sorted(list(map(int,input().split())))
print(min(nums[i+1]-nums[i] for i in range(len(nums)-1)))
