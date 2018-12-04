count = 0

def merge_sort(li):

    if len(li) < 2: return li
    m = len(li) / 2
    return merge(merge_sort(li[:m]), merge_sort(li[m:]))

def merge(l, r):
    global count
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            count = count + (len(l) - i)
            j += 1
    result.extend(l[i:])
    result.extend(r[j:])
    return result


num_inversions = [10, 2, 3, 22, 33, 7, 4, 1, 5]
print merge_sort( num_inversions)
print count


