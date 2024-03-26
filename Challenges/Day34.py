def removeTrailingZeros(num):
    num=num[::-1]
    num=int(num)
    num=str(num)
    num=num[::-1]
    return num

num = "51230100"
print(removeTrailingZeros(num))