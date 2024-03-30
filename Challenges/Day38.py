def searchRange(nums,target):
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            first = i
            break
    for i in reversed(range(len(nums))):
        if nums[i] == target:
            last = i
            break
    return [first,last]

nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums,target))