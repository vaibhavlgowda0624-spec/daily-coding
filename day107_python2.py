nums=list(map(int,input().split()))

evens=[n for n in nums if n%2==0]

print(max(evens))
