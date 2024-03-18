def applyOperations(nums):
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] += nums[i+1]
            nums[i+1] = 0
    zeros = nums.count(0)
    nums = [value for value in nums if value != 0]
    return nums + [0] * zeros

nums = [1,2,2,1,1,0]
print(applyOperations(nums))