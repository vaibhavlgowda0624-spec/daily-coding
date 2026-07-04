nums=[1,2,2,3,3,4]

for n in set(nums):
    if nums.count(n)>1:
        print(n)
