from collections import defaultdict
pair = frozenset([('A','U'),('G','C'),('G','U'),('U','A'),('C','G'),('U','G')])
def best(squence):
    global pair
    table = defaultdict(tuple)
    opt = defaultdict(int)
    end = len(squence)
    for i in xrange(len(squence)):
        table[i, i + 1] = squence[i]

    for i in xrange(0, len(squence)):
        opt[i, i+1] = 0
        opt[i, i] = 0
    opt[end, end] = 0

    for span in xrange(2, end+1):
        for i in xrange(end-span+1):
            j = i + span
            if(table[i, i+1], table[j-1, j]) in pair:
                opt[i, j] = opt[i+1, j-1] + 1
            for k in xrange(i+1, j):
                if opt[i, k] + opt[k, j] > opt[i, j]:
                    opt[i, j] = opt[i, k] + opt[k, j]
    result = opt[0, end]

    def parse(x, y):
        if x == y:
            return []
        if x + 1 == y:
            return ['.']
        flag = False
        for k in xrange(x + 1, y):
            if opt[x, k] + opt[k, y] == opt[x, y]:
                flag = True
                break
        if flag is False:
            if(table[x, x+1], table[y-1, y]) in pair:
                return ['('] + parse(x+1, y-1) + [')']
            else:
                print "error"
        return parse(x, k) + parse(k, y)
    STR = ''.join(parse(0, len(squence)))
    return result, STR

print best("GCACG")
print best("UUCAGGA")
print best("GUUAGAGUCU")
print best("AACCGCUGUGUCAAGCCCAUCCUGCCUUGUU")
print best("CAUCGGGGUCUGAGAUGGCCAUGAAGGGCACGUACUGUUU")
print best("AGGCAUCAAACCCUGCAUGGGAGCG")