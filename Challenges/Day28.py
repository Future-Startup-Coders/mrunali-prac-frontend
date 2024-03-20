def sortedSquare(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    nums.sort()
    return nums

nums =[-4,-1,0,3,10]
print(sortedSquare(nums))