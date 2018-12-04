from collections import defaultdict
pair = frozenset([('A','U'),('G','C'),('G','U'),('U','A'),('C','G'),('U','G')])
def total(squence):
    global pair
    table = defaultdict(tuple)

    for i in xrange(len(squence)):
        table[i, i+1] = squence[i]

    tot = defaultdict(int)
    end = len(squence)

    for i in xrange(0, len(squence)):
        tot[i, i+1] = 1
        tot[i, i] = 1
    tot[end, end] = 1

    for span in xrange(2, end+1):
        for i in xrange(end-span+1):
            j = i + span
            tot[i, j] += tot[i+1, j]
            for k in xrange(i+1, j+1):
                if(table[i, i+1], table[k-1, k]) in pair:
                    tot[i, j] += tot[i+1, k-1] * tot[k, j]

    return tot[0, end]


print total("UUCAGGA")
print total("UUGGACUUG")
print total("UUUGGCACUA")
print total("GAUGCCGUGUAGUCCAAAGACUUC")
print total("AGGCAUCAAACCCUGCAUGGGAGCG")
