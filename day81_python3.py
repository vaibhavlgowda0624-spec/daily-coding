nums = list(map(int,input().split()))

even = sum(n%2==0 for n in nums)
odd = len(nums)-even

print(even, odd)
