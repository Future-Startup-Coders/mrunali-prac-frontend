def lengthOfLastWord(s):
    s = s.strip()
    count = 0
    for i in s[::-1]:
        if i == ' ':
            break
        count +=1
    return count


s = "  Hello   World  "
print(lengthOfLastWord(s))