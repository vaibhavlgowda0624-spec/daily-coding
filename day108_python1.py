num=int(input())

s=sum(int(d)**len(str(num)) for d in str(num))

print(s==num)
