import bisect
def find(array, key, k):
    result = []
    mark = bisect.bisect(array, key)
    i = mark
    j = mark
    for x in range(0, k):
        if(i == 0):
            result += [array[j]]
            j += 1
        elif(i > 0):
            if(abs(array[i-1]-key)<=abs(array[j]-key)):
                result = [array[i-1]] + result
                i -= 1
            else:
                result.append(array[j])
                if(j<len(array)-1):
                    j += 1
                else:
                    result[0:0] = array[i-1:i-(k-x):-1]
                    break
    return result

print find([1, 2, 4, 5, 5, 6, 8, 9, 11, 12], 5, 3)
print find([1, 2, 3, 4, 4, 6, 6, 8, 9, 11, 12], 6, 3)
print find([1, 2, 3, 4, 4, 6, 6, 7.8, 8, 9, 10.1, 10.5, 11, 12], 9, 3)
