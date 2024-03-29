def firstUniqChar(s):
    s_str ={}
    index = 0
    for i in s:
        if i in s_str:
            s_str[i] +=1
        else :
            s_str[i]=1
    for i in range(len(s)):
        if s_str[s[i]] ==1:
            return i
    return -1
s = "leetcode"
print(firstUniqChar(s))