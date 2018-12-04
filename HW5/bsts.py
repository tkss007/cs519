def bsts(n):
    if n <= 1:
        return 1

    res = 0
    for i in range(n):
        res += bsts(i) * bsts(n - i - 1)

    return res

for i in range(10):
    print bsts(i)
