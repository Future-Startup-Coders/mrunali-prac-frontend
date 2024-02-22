# Given number is palindrome or not
def is_palindrome(num):
    return num== num[::-1]

input = input("Enter NUmber : ")
print("Output : ",is_palindrome(input) )