def reverseVowels(s):
    s = list(s)
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    l , r = 0, len(s)-1
    while l <r:
        if s[l] in vowels:
            while True:
                if s[r] in vowels:
                    s[l],s[r] = s[r],s[l]
                    r-=1
                    break
                r=r-1
        l+=1

    return ''.join(s)

        
s = "hello"
print(reverseVowels(s))