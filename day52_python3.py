nums = list(map(int,input().split()))
res = []

for n in nums:
    if n not in res:
        res.append(n)

print(res)
