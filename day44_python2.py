nums = list(map(int,input().split()))
print(max(set(nums), key=nums.count))
