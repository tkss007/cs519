#!/usr/bin/env python

def mergesort(lst):
    if (len(lst) <= 1): return lst
    left = mergesort(lst[:len(lst) / 2])
    right = mergesort(lst[len(lst) / 2:len(lst)])
    result = []
    while len(left) > 0 and len(right) > 0:
        if (left[0] > right[0]):
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    if (len(left) > 0):
        result.extend(mergesort(left))
    else:
        result.extend(mergesort(right))
    return result


def main():
    L = [22, 11, 11, 55, 33, 66]
    print mergesort(L)


if __name__ == "__main__":
    main()