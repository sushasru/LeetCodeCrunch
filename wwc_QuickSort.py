#QuickSort
def qsort(arr,sindex,eindex):
    if sindex<eindex:
        print("len(arr):",len(arr))
        mid = int(len(arr)/2)
        print("\nMid index: {}; Mid val:{}".format(mid,arr[mid]))
        pv = qpvsort(arr,sindex,eindex)
        print("HERE")
        qsort(arr, sindex, pv-1)
        print("HEREHERE")
        qsort(arr,pv+1,eindex)
    
    
def qpvsort(arr,s, e):
    i = s
    p = s
    pivot = arr[e]
    print("\ni: {}, p: {}, e: {}, pivot:{}, arr:{}".format(i,p,e,pivot,arr[s:e+1]))
    while i < e and p < e:
        print("\ti:{},p:{}".format(i,p))
        print("\t\tIs {} <= {}".format(arr[i],pivot))
        if arr[i] <= pivot:
            print("\t\t\tYES!! SWAP WITH ELEMENT AT THE START POINTER")
            temp = arr[i]
            arr[i] = arr[p]
            arr[p] = temp
            i += 1
            p += 1
            print("\t\t\tcur array:",arr[s:e+1])
        else:
            print("\t\t\tNO!! MOVE ON!")
            i += 1
    if p < e:
        arr[e] = arr[p]
        arr[p] = pivot
        print("\t\t\tcur array:",arr[s:e+1])
    print("\tNew Pv is :",p)
    return p
            
    





arr = [3,44,38,5,37,15,36,27,2,46,4,19,50,48]
print("array to be sorted:",arr)
qsort(arr,0,len(arr)-1)
print("sorted array:",arr)
print("**************************************************")
##arr = [4,5,3,7,9,8]
##print("array to be sorted:",arr)
##qsort(arr,0,len(arr)-1)
##print("sorted array:",arr)
