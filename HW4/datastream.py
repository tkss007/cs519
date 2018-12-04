import heapq
def ksmallest(k, l):
    max_heap = []
    length = len(l)
    if not l or k <= 0 or k > length:
        return
    k = k - 1
    for element in l:
        element = -element
        if len(max_heap) <= k:
            heapq.heappush(max_heap, element)
        else:
            heapq.heappushpop(max_heap, element)

    return sorted(map(lambda x: - x, max_heap))

print ksmallest(3, [10, 2, 9, 3, 7, 8, 11, 4, 5, 7])
print ksmallest(4, [10, 2, 9, 3, 7, 2, 8, 11, 2, 4, 5, 7])
print ksmallest(4, [10, 2, 9, 3, 7, 2, 8, 11, 2, 4, 5, 7, -1])
print ksmallest(4, [10, 2, 9, 3, 7, 2, 8, 11, 2, 0, 4, 5, 7, -1])
print ksmallest(3, xrange(1000000, 0, -1))

