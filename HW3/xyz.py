from bisect import bisect_left
number = []

def _find(l1, x, k):
    pos = bisect_left(l1, x)
    if pos == 0:
        return l1[0]
    if pos == len(l1):
        return l1[-1]
    before = l1[pos - 1]
    after = l1[pos]
    if after - x < x - before:
        l1.remove(after)
        return after
    else:
        l1.remove(before)
        return before
def find(l1, x, k):
    global number
   # i = 0
    for i in range(0, k):
        number = number + [_find(l1, x, k)]
    return number

l = [1, 5, 4, 5, 6, 4, 9, 3, 12]
print find(l, 5, 3)
