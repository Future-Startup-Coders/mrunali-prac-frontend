def frequencySort(s):
    f = []
    for i in set(s):
        f.append([s.count(i) , i])
    res = ''
    f.sort()
    print(f)
    for i in f[::-1]:
        res += str(i[1] * i[0])
    return res

s= "tree"
print(frequencySort(s))