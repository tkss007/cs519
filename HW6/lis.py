l1 = []
def choose_item(weight, idx, cache):
    if idx < 0:
        return 0, []

    k = (weight, idx)
    if k in cache:
        return cache[k]

    w, v, qty = items[idx]
    best_v, best_list = 0, []

    for i in range(0, qty + 1):
        wlim = weight - i * w
        if wlim < 0:
            break

        val, taken = choose_item(wlim, idx - 1, cache)
        if val + i * v > best_v:
            best_v = val + i * v
            best_list = taken[:]
            best_list.append(i)

    cache[k] = [best_v, best_list]

    return best_v, best_list

def best(max, l):
    global items
    global l1
    l1 = []
    items = l
    v, lst = choose_item(max, len(items) - 1, {})
    for i, cnt in enumerate(lst):
        if cnt > 0:
           #print cnt
            l1 = l1 + [cnt]
        else:
            l1.append(0)
    return v, l1


#items = [(1, 10, 6), (3, 15, 4), (2, 10, 3)]
#print best(15, items)


#print best([(2, 4, 2), (3, 5, 3)], 3)
#print best([(1, 5, 2), (1, 5, 3)], 3)
#print best([(1, 5, 1), (1, 5, 3)], 3)
#print best([(1, 10, 6), (3, 15, 4), (2, 10, 3)], 20)
#print best([(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)], 92)

print best(3, [(2, 4, 2), (3, 5, 3)])
print best(3, [(1, 5, 2), (1, 5, 3)])
print best(3, [(1, 5, 1), (1, 5, 3)])
print best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
print best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
