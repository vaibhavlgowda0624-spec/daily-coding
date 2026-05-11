nums = [1,2,3,4,5]
target = 4

low, high = 0, len(nums)-1

while low <= high:
    mid = (low + high)//2
    
    if nums[mid] == target:
        print("Found")
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
