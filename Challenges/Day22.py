def mySqrt(x):
    num = 1
    while (num*num<=x):
        num+=1
    return num-1

x  = 9
print(mySqrt(x))