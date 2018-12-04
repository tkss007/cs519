maxValue = 0
def _longest(array):
    global maxValue
    if array == []:
        return -1
    maxLeft = _longest(array[0]) + 1
    maxRight = _longest(array[2]) + 1
    if (maxLeft + maxRight +1) > maxValue:
        maxValue = maxLeft + maxRight
    if maxLeft > maxRight:
        return maxLeft
    else:
        return maxRight

def longest(array):
    global maxValue
    maxValue = 0
    longest_path = _longest(array)
    if maxValue > longest_path:
        return maxValue
    else:
        return longest_path

print longest([[], 1, []])
print longest([[[], 1, []], 2, [[], 3, []]])
print longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]])
print longest([[[], 2, [[], 3, []]], 4, [[[[[], 4, []], 4, []], 5, []], 6, [[], 7, [[], 9, []]]]])