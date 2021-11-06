#Quick Sort
def QSort(ar,si,ei):
    print("\nQuickSort:")
    print("\tar:{},si:{},ei:{}".format(ar,si,ei))
    if si<ei:
        pv = GetPivot(ar,si,ei)
        QSort(ar,si,pv-1)
        QSort(ar,pv+1,ei)
    return ar

def GetPivot(ar,si,ei):
    print("\nGetPivot")
    i = si
    pv = si
    pVal = ar[ei]
    print("\tInitial values:\n\t\tsi:{},ei:{},i:{},pv:{},pVal:{}".format(si,ei,i,pv,pVal))
    while i<ei and pv<ei:
        print("\t\tIs ar[{}]:{}<ar[{}]:{}?".format(i,ar[i],ei,ar[ei]))
        if ar[i] <= pVal:
            print("\t\t\tYES!SWAP!")
            ar[i],ar[pv] = ar[pv],ar[i]
            i += 1
            si += 1
            pv += 1
            print("\t\t\tUpdated Array:",ar)
        else:
            i += 1
        print("\tUpdated values:\n\t\tsi:{},ei:{},i:{},pv:{},pVal:{}".format(si,ei,i,pv,pVal))
    if pv < ei:
        ar[ei],ar[pv] = ar[pv],ar[ei]
    print("\tCur Array:",ar)
    print("\tPivot index:",pv)
    return pv
        
            
    
    



ar = [3,44,38,5,37,15,36,27,2,46,4,19,50,48]
print("Array to sort:", ar)
print("Sorted Array:",QSort(ar,0,len(ar)-1))
print("*******************************************")
