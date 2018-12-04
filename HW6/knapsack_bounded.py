def best(W, l):
    Item_list = l
    Value_list = [0 for _ in xrange(W + 1)]
    Pick_list = [[0 for _ in xrange(len(Item_list))] for _ in xrange(W + 1)]

    for i in xrange(len(Item_list)):
        process(i, Value_list, Item_list, Pick_list, W)
    result1 = max(Value_list)
    index = Value_list.index(result1)
    result = (result1, Pick_list[index])
    return result


def process(i, Value_list, Item_list, Pick_list, W):
    weight = Item_list[i][0]
    value = Item_list[i][1]
    for y in xrange(Item_list[i][2]):
        for x in xrange(W, weight - 1, -1):
            number = Item_list[i][2]
            number_pick = Pick_list[x - weight][i]
            if Value_list[x - weight] + value > Value_list[x]:
                Value_list[x] = Value_list[x - weight] + value
                Pick_list[x] = Pick_list[x - weight][:]
                Pick_list[x][i] += 1

print best(3, [(2, 4, 2), (3, 5, 3)])
print best(3, [(1, 5, 2), (1, 5, 3)])
print best(3, [(1, 5, 1), (1, 5, 3)])
print best(20, [(1, 10, 6), (3, 15, 4), (2, 10, 3)])
print best(92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)])
