# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i+=1
                nums[i]=nums[j]
                j+=1
            elif nums[i]==nums[j]:
                j+=1
        return i+1


def removeDuplicate(nums):
    a = []
    for i in nums:
        if i not in a:
            a.append(i)
    return a

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicate(nums))