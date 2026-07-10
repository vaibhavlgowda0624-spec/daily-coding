num = input()

count = sum(int(d) % 2 == 0 for d in num)

print(count)
