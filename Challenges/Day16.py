def reverse(x):
    reverse = int(str(abs(x))[::-1])
    limit = 2**31
    if x < 0 and reverse <= limit:
        return - reverse
    if x > 0 and reverse < limit:
        return reverse
    return 0

x = 123
print(reverse(x))