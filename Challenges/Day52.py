def fib(n):
    prevNum = 0
    currentNum = 1
    for i in range(0, n-1):
        prevPrevNum = prevNum
        prevNum = currentNum
        currentNum = prevNum + prevPrevNum
    return currentNum

n = 3
print(fib(n))