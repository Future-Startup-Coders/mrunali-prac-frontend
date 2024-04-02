def sumOfUnique(nums):
    sum = 0 
    for i in nums:
        if nums.count(i) ==1:
            sum+=i
    return sum

nums = [1,2,3,2]
print(sumOfUnique(nums))