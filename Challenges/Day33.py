def reverseWords(s):
    a = s.split()
    return " ".join(a[::-1])


s = "the sky is blue"
print(reverseWords(s))