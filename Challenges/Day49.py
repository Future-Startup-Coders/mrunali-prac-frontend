def removeDuplicates(nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


nums = [1,1,2]
print(removeDuplicates(nums))