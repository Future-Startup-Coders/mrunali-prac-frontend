def numberGame(nums):
    nums.sort()
    i = 0
    while(i <len(nums)):
        nums[i],nums[i+1]=nums[i+1],nums[i]
        i +=2
    return nums

nums = [5,4,2,3]
print(numberGame(nums))