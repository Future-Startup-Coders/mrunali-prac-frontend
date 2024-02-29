def singleNumber(nums):
    ans = 0
    for i in nums:
        ans = ans ^ i
    return ans

nums = [4,1,2,1,2]
print(singleNumber(nums))