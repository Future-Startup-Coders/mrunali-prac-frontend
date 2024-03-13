def firstBadVersion(n):
    def isBadVersion(version):
        return version >= bad
    l = 1
    r = n
    while (l<=r):
        mid = (l+r)//2
        if isBadVersion(mid):
            r = mid-1
        else:
            l = mid+1
    return l

n = 5
bad = 1
print(firstBadVersion(n))