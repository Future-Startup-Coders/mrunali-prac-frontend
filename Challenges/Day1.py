# Twosum
def return_indices(nums, target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return(i,j)
    
nums= [2,7,11,15]
target = 9
print("Output: ", return_indices(nums,target))