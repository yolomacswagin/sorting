def swap(alist, index):
    a = alist[index]
    b = alist[index+1]
    alist[index] = b
    alist[index+1] = a
    return (alist)

def bsort(alist):
    swaps = True
    while swaps:
        swaps = False
        for i in range(len(alist)-1):
            if (alist[i] > alist[i+1]):
                alist = swap(alist, i)
                swaps = True
    return (alist)