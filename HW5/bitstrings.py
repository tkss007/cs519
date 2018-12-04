#def fib2(n, cache=None):
 #   if cache is None:
  #      cache = {}

#    if n in cache:
 #       return cache[n]

#    cache[n] = 1 if n <= 2 else fib2(n - 1, cache) + fib2(n - 2, cache)

 #   return cache[n]


#print [fib2(i) for i in xrange(1, 11)]
sum1 = 0
def _max_wis(l, i = 0, j = 0):
    for n in xrange(0, len(l) - 1):

         if (i == 0 or j == 0):
             j = i
             i = l[n]
             sum1 = max(i, j)
             return sum1
         else:
             temp = i
             i = j + l[n]
             j = temp
             sum1 = max(i, j)
             return sum1

def max_wis(l):
    global sum1
    value = 0
    value = value + _max_wis(l)

l = [7, 8, 5, 4, 9, 10, 2, 3, -7, 6]
print max_wis(l)
