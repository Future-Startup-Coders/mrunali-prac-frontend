def lengthOfLongestSubstring(s):
    d = {}
    max_length = start = 0
    for i in range(len(s)):
        if s[i] in d and start <= d[s[i]]:
            start = d[s[i]] +1
        else:
            max_length = max(max_length, i- start +1)
        d[s[i]] = i
    return max_length

s = "abcabcbb"
print(lengthOfLongestSubstring(s))