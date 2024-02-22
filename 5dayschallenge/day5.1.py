# A function that returns a list where the ith element is the sum of the first i+1 elements of nums

nums = [1,2,3,4,5]
lst = []
sum_no = 0
for i in range(0,len(nums)):
    sum_no = sum_no + nums[i]
    lst.append(sum_no)
print("Output : ",lst)