def binsearch(slist,n):
    print("list to search:",slist)
    for i,val in enumerate(slist):
        if val == n:
            return i
    return -1

def recbinsearch(lst,n):
    mid = int(len(lst)/2)
    st = 0
    ed = len(lst)

    while st < ed:
        mid = (st+ed)//2

        if lst[mid] == n:
            print("1) {} is at {}".format(n,mid))
            return mid
        elif lst[mid] < n:
            print("2) {} is > {}".format(n,mid))
            st = mid
        else:
            print("3) {} is < {}".format(n,mid))
            st = 0
            ed = mid
        st += 1
        
    return -1 



n = 10
lst = [1,2,3,4,5,6,7,8,9,10]
print("{} is at {} in {}".format(n,recbinsearch(lst,n),lst))
