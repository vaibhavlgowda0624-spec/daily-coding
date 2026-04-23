nums = []

for n in range(2,50):
    if all(n%i!=0 for i in range(2,n)):
        nums.append(n)

print(nums)
