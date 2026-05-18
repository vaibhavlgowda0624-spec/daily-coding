with open("numbers.txt") as f:
    nums = list(map(int, f.read().split()))
    
print(max(nums))
