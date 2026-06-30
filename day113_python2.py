nums=list(map(int,input().split()))

for n in nums:
    if n>1 and all(n%i!=0 for i in range(2,n)):
        print(n)
