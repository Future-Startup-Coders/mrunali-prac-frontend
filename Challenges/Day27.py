def runningSum(nums):
    answerList = []
    sumValue = 0
    for i in range(len(nums)):
        sumValue = sumValue + nums[i]
        answerList.append(sumValue)
    return answerList

nums = [1,2,3,4]
print(runningSum(nums))