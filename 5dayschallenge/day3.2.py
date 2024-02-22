# Sum of digit of given number
def sum_of_digit(num):
    sum = 0
    while (num>0):
        sum = sum+ num%10   #% gives remainder so here num%10 , it will consider remainder e.g 248%10 = 8
        num = num//10        # // it will remove points from the no e.g 248 / 10 ==24.8 and , 248//10 = 24
    return sum
num1 = int(input("Enter Number : "))
print("sum fo digits : ",sum_of_digit(num1))