def reverseOnlyLetters(s):
    s1='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l= 0
    r=len(s)-1
    s= list(s)
    while l<r:
        if s[l] in s1:
            if s[r] in s1:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            else:
                r-=1
        else:
            l+=1
    return ''.join(s)   # Convert the list back to a string

s = "ab-cd"
print(reverseOnlyLetters(s))