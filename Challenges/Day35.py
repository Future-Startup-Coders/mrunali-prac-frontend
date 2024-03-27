def isPalindrome(s):
    str_s = ""
    for i in s:
        if i.isalnum():
            str_s += i
    str_s = str_s.lower()
    return str_s == str_s[::-1]

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))