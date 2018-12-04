def best(total, coins_list):
    s = [0]
    Pick_list = [[0 for _ in xrange(len(coins_list))] for _ in xrange(total + 1)]
    for i in range(1, total+1):
        s.append(-1)
        for coin_val in coins_list:
            for x in xrange(len(coins_list)):
                if i-coin_val >= 0 and s[i-coin_val] != -1 and (s[i] > s[i-coin_val] or s[i] == -1):
                    s[i] = 1 + s[i - coin_val]
                    Pick_list[i] = Pick_list[i - coins_list[x]][:]
                    Pick_list[i][x] += 1



    if s[i] == -1:
        return None
    else:
        return s[total], Pick_list[total]

print best(11, [1, 3, 5])
print best(12, [2, 7, 5])
print best(12, [3, 4, 5])
print best(47, [6, 10, 15])
print best(59, [6, 10, 15])
print best(37, [4, 6, 15])
print best(27, [4, 6, 15])
print best(75, [4, 6, 15])
print best(17, [2, 4, 6])

