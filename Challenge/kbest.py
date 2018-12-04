from collections import defaultdict
pair = frozenset([('A','U'),('G','C'),('G','U'),('U','A'),('C','G'),('U','G')])
def kbest(squence):
    global pair
    table = defaultdict(tuple)
    opt = defaultdict(int)
    end = len(squence)