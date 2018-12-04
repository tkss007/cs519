from math import ceil
def merge(all_lst):
    sorted_lst = []
    while all_lst:
        min_value,index = all_lst[0][0],0
        for lst in all_lst:
            if lst[0]<min_value:
                min_value = lst[0]
                index = all_lst.index(lst)
        sorted_lst.append(min_value)
        all_lst[index].pop(0)
        if not all_lst[index]:
            all_lst.remove(all_lst[index])
    return sorted_lst


def kmergesort(l, k):
    def split(l):
        split_l = []
        j = ceil(len(l)/k) if len(l) >= k else 1
        for i in range(0, len(l), j):
            split_l.append(l[i:i+j])
        return split_l
    l = split(l)
    if len(l[0]) == 1:
        return l
    else:
        for i in range(len(l)):
            l[i] = merge(kmergesort(l[i], k))
        return merge(l)

print kmergesort([4, 1, 5, 2, 6, 3, 7, 0], 3)

