def climbStairs(n):
    n1, n2 = 0, 1
    for i in range(n):
        res = n1 + n2
        n1 = n2
        n2 = res
    return res

n = 2
print(climbStairs(n))