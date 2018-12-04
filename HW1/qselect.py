import random
def qselect(a_list, left, right, k):
    if left == right:
        return a_list[left]

    split = partition(a_list, left, right)
    length = split - left + 1

    if length == k:
        return a_list[split]
    elif length > k:
        return qselect(a_list, left, split - 1, k)
    else:
        return qselect(a_list, split + 1, right, k - length)

def random_partition(a_list, left, right):
    split = random.randint(left, right)
    temp = a_list[left]
    a_list[left] = a_list[split]
    a_list[split] = temp
    return partition(a_list, left, right)

def partition(a_list, left, right):
    if left == right:
        return a_list
    x = a_list[left]
    index1 = left + 1
    for index2 in range(left + 1, right + 1):
        if a_list[index2] <= x:
            temp = a_list[index1]
            a_list[index1] = a_list[index2]
            a_list[index2] = temp
            index1 += 1
    temp = a_list[left]
    a_list[left] = a_list[index1 - 1]
    a_list[index1 - 1] = temp
    return index1 - 1

'''
def quick_sort(a_list, left, right):
    if left < right:
        q = partition(a_list, left, right)
        quick_sort(a_list, left, q - 1)
        quick_sort(a_list, q + 1, right)

#a_list = [11, 8, 4, 11, 5, 2, 7, 9]
'''
a_list = []
for x in range(20):
    a_list.append(random.randint(0, 100))
print a_list
#quick_sort(a_list, 0, len(a_list) - 1)
#print (quick_sort(a_list, 0, len(a_list) - 1))
k = random.randint(1, 21)
#print 'You choose the %dth munber in this list'%k
#print 'The nuber is:'
print(qselect(a_list, 0, len(a_list) - 1, k))




