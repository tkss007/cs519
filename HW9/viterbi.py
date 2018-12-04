from collections import defaultdict

def longest(n,edge):
    S = defaultdict(set)
    for u, v in edge:
        S[u].add(v)
    order_list = []
    visit_set = set()
    Isacycle = [False]

    def DFS(u):
        V = S[u]
        for i in V:
            if i in order_list:
                continue
            else:
                if i in visit_set:
                    Isacycle[0] = True
                    return
                else:
                    visit_set.add(i)
                    DFS(i)
        order_list.insert(0, u)

    for i in xrange(n):
        if i not in visit_set:
            DFS(i)

    pathCost = defaultdict(lambda: [None, 0])

    for i in order_list:
        for j in S[i]:
            if pathCost[j][1] < pathCost[i][1] + 1:
                pathCost[j][1] = pathCost[i][1] + 1
                pathCost[j][0] = i
    def solution():
        index = max(pathCost, key=lambda x: pathCost[x][1])
        value = pathCost[index][1]
        trace = []
        while index is not None:
            trace.insert(0, index)
            index = pathCost[index][0]
        return value, trace

    return solution()

print longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)])
print longest(8, [(0,2), (1,2), (2,3), (2,4), (4,3), (3,5), (4,5), (5,6), (5,7)])