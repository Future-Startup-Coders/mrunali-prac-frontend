def findDuplicate(nums):
    a = set()
    for i in nums:
        if i in a:
            return i
        else:
            a.add(i)

nums = [1,3,4,2,2]
print(findDuplicate(nums))