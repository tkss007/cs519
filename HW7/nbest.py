from heapq import heappush, heappop
def nbest(ABs):
    k = len(ABs)
    n = len(ABs[0][0])
    def trypush(i, p, q):
        A, B = ABs[i]
        if p < n and q < n and (i, p, q) not in used:
            heappush(h, (A[p] + B[q], i, p, q, (A[p],B[q])))
            used.add((i, p, q))
    h, used = [], set()
    for i in xrange(k):
        trypush(i, 0, 0)
    for _ in xrange(n):
        _, i, p, q, pair = heappop(h)
        yield pair
        trypush(i, p + 1, q)
        trypush(i, p, q + 1)

