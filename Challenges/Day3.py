def searchInsert(nums,target):
    i=0
    for i in range (0, len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] < target :
            i+=1
        else:
            nums[i]> target
            return i
            
    return i