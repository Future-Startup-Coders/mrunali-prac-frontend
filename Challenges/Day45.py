def findPeakElement(nums):
    for i in range(0,len(nums)-1):
        if nums[i] > nums[i+1]:
            return i
    return len(nums)-1

nums = [1,2,3,5,6,4]
print(findPeakElement(nums))