def addDigits(num):
    while num>=10:
        num = sum(int(i) for i in str(num))
    return num


num = 38
print(addDigits(num))