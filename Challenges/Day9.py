def findPeakElement(nums):
    n = len(nums)-1
    for i in range(0,n):
        if nums[i] > nums[i+1]:
            return i
    return n
            
nums = [1,2,3,1]
print(findPeakElement(nums))