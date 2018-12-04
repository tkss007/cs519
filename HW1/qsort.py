import random
def qsort(l):
    if l == []:
        return []
    else:
        pivot = l[0]
        left = [x for x in l if x < pivot]
        right = [x for x in l[1:] if x >= pivot]
        return [qsort(left)] + [pivot] + [qsort(right)]

def _search(l, x):
    if l == []:
        return l
    if l[1] == x:
        return x
    elif l[1] > x:
        return _search(l[0], x)
    else:
        return _search(l[2], x)

def search(l, x):
    if _search(l, x) == []:
        return False
    else:
        return True

def insert(l, x):
    l1 = _search(l, x)
    if l1 == []:
        l1 += ([[]] + [x] + [[]])

def sorted(l):
    if l == []:
        return []
    return sorted(l[0]) + [l[1]] + sorted(l[2])

l = qsort([4, 2, 6, 3, 5, 7, 1, 9])
print "The tree is:" + str(l)
print "Search(tree, 6.5) is" + str(search(l, 6.5))
print "Search(tree, 6) is" + str(search(l, 6))
insert(l, 6.5)
print "New tree"
print sorted(l)
