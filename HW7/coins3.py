def best(v, l):
    i1 = l[0]
    j1 = l[1]
    k1 = l[2]
    l1 = [0, 0, 0]
    sum = 0
    for i in range(0, v/i1 + 1):
        for j in range(0, v/j1 + 1):
            for k in range(0, v/k1 + 1):
                if (l[0]*i + l[1]*j + l[2]*k == v):
                    if sum > (i + j + k) or sum == 0:
                        if i != 0:
                            sum = 1
                            l1[0] = i
                            if j != 0:
                                sum = sum + 1
                                l1[1] = j
                                if k != 0:
                                    sum = sum + 1
                                    l1[2] = k
                        elif j != 0:
                            sum = 1
                            l1[1] = j
                            if k != 0:
                                sum = sum + 1
                                l1[2] = k
                        elif k != 0:
                            sum = 1
                            l1[2] = k

    if sum != 0:
        return sum, l1
    else:
        return None

#print best(11, [4, 2, 6])
print best(47, [6, 10, 15])
print best(59, [6, 10, 15])
print best(37, [4, 6, 15])
print best(27, [4, 6, 15])
print best(75, [4, 6, 15])
print best(17, [2, 4, 6])

