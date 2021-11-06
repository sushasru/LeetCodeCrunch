#MergeSort
def merge(lst):
    ln = len(lst)
    if ln>1:
        mid = int(ln/2)
        la = merge(lst[:mid])
        ra = merge(lst[mid:])
        msort(la,ra,lst)
    return lst

def msort(la,ra,lst):
    li = 0
    ri = 0
    i = 0

    lalen = len(la)
    ralen = len(ra)

    while li < lalen and ri < ralen:
        if la[li] < ra[ri]:
            lst[i] = la[li]
            i += 1
            li += 1
        else:
            lst[i] = ra[ri]
            i += 1
            ri += 1
    while li < lalen:
        lst[i] = la[li]
        i += 1
        li += 1
    while ri < ralen:
        lst[i] = ra[ri]
        i += 1
        ri += 1
    return lst
        





lst = [0,8,1,2,7,9,3,4]
print("Array to sort:",lst)
print(merge(lst))
