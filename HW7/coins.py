def best(V, l):
    table = [[float('inf') for _ in xrange(V+1)] for _ in xrange(len(l))]
    for i in xrange(len(l)):
        table[i][0] = 0
    for i in xrange(len(l)):
        for j in xrange(1, V+1):
            if j % l[i] == 0:
                table[i][j] = 1
            else:
                pre_v = j - l[i]
                if(pre_v < 0):
                    continue
                if table[i][pre_v] == float('inf'):
                    min = float('inf')
                    for k in xrange(i):
                        if min > table[k][pre_v]:
                            min = table[k][pre_v]
                    table[i][j] = min + 1
                else:
                    table[i][j] = table[i][pre_v]

    def solution(table, V):
        min = float('inf')
        result = [0 for _ in xrange(len(l))]
        for i in xrange(len(l)):
            if min > table[i][V]:
                min = table[i][V]
                start = i
        if min == float('inf'):
            return None
        j = V
        index = start
        while j is not 0:
            result[index] += 1
            j = j - l[index]
            if table[index][j] == float('inf'):
                for i in xrange(index):
                    if table[index][j] > table[i][j]:
                        index = i
        return table[start][V], result

    return solution(table, V)

print best(47, [6, 10, 15])
print best(59, [6, 10, 15])
print best(37, [4, 6, 15])
print best(27, [4, 6, 15])
print best(75, [4, 6, 15])
print best(17, [2, 4, 6])
