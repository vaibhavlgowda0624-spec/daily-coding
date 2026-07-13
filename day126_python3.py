start = int(input("Start: "))
end = int(input("End: "))

for num in range(start, end + 1):
    power = len(str(num))
    total = sum(int(d) ** power for d in str(num))
    if total == num:
        print(num)
