def max_wis(l):
    l2 = []
    sum_l2 = []

    return [_max_wis(l, (len(l) - 1), l2, sum_l2), l2[len(l) - 1]]

def _max_wis(l, n, l2, sum_l2):
    if len(l) == 0:
        sum_l2.append(0)
        l2.append([])
        return sum_l2[n]

    if n < len(sum_l2):
        return sum_l2[n]

    if n == 0:
        if l[n] > 0:
            sum_l2.append(l[n])
            l2.append([l[n]])
        else:
            sum_l2.append(0)
            l2.append([])
    elif n == 1:
        if l[n] > _max_wis(l, n - 1, l2, sum_l2):
            sum_l2.append(l[n])
            l2.append([l[n]])
        else:
            sum_l2.append(sum_l2[n - 1])
            l2.append(l2[n - 1][:])
    else:
        if l[n] + _max_wis(l, n - 2, l2, sum_l2) > _max_wis(l, n-1, l2, sum_l2):
            sum_l2.append(sum_l2[n - 2] + l[n])
            l2.append(l2[n - 2] + [l[n]])
        else:
            sum_l2.append(sum_l2[n - 1])
            l2.append(l2[n - 1][:])
    return sum_l2[n]

def max_wis2(l):
    l1 = [[], []]
    sum_l1 = [0, 0]
    for n in xrange(len(l)):
        if (l[n] + sum_l1[n % 2 - 2]) > sum_l1[n % 2 - 1]:
            sum_l1[n % 2] = l[n] + sum_l1[n % 2 - 2]
            l1[n % 2].append(l[n])
        else:
            sum_l1[n % 2] = sum_l1[n % 2 - 1]
            l1[n % 2] = l1[n % 2 - 1][:]
    return [sum_l1[(len(l) - 1) % 2], l1[(len(l) - 1) % 2]]

print max_wis([7, 8, 5, 4, 9, 10, 2, 3, -7, 6])
print max_wis([2, 7, 4, 3, -9, 8, 6, 5])
print max_wis([7, 8, 5, 4, 9, 10, 2, 3, -7, 6, 2, 7, 4, 3, -9, 8, 6, 5])
print max_wis([3, 4])
print max_wis([2])
print max_wis([])
print max_wis([-3, -4])

print max_wis2([7, 8, 5, 4, 9, 10, 2, 3, -7, 6])
print max_wis2([2, 7, 4, 3, -9, 8, 6, 5])
print max_wis2([7, 8, 5, 4, 9, 10, 2, 3, -7, 6, 2, 7, 4, 3, -9, 8, 6, 5])
print max_wis2([3, 4])
print max_wis2([2])
print max_wis2([])
print max_wis2([-3, -4])

