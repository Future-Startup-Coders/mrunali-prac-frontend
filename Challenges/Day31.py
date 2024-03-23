def containsDuplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return True
    return False

nums= [1,2,3,1]
print(containsDuplicate(nums))