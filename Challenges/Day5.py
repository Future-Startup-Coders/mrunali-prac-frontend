def missingNumber(nums):
    n = len(nums)
    res = n*(n+1)//2
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
    return (res-sum)

nums = [ 0,1,2,3,4,6,7,8,9]
print(missingNumber(nums))