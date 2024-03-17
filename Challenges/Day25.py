def majorityElement(nums):
    count = 0
    a = 0
    for i in nums:
        if count == 0:
            a = i
        if i == a:
            count+=1
        else:
            count-=1
    return a

        

nums = [3,2,3]
print(majorityElement(nums))