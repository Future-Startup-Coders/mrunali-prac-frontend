def isPalindrome(x):
    if (str(x) ==  str(x)[::-1]):
        return True
    return False

x = 121121
print(isPalindrome(x))