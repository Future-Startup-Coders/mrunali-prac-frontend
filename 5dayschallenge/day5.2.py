# Program to calculate the sum of even and odd digits in a number

num = 12345
sum_even = 0
sum_odd = 0

for i in str(num):
    i = int(i)
    if i % 2 ==0:
        sum_even = sum_even + i 
    else :
        sum_odd = sum_odd + i 
        
print("Sum of even digits: ",sum_even)
print("Sum of odd digits: ",sum_odd)