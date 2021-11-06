def MSort(OA):
    mid = len(OA)/2
    LA = []
    RA = []
    if len(OA)>1:
        LA = OA[0:int(mid)]
        RA = OA[int(mid):]
        MSort(LA)
        MSort(RA)
        Merge(OA,LA,RA)

def Merge(O,L,R):
    Oi = 0
    Li = 0
    Ri = 0
    while Li < len(L) and Ri < len(R):
        if L[Li] < R[Ri]:
            O[Oi] = L[Li]
            Li += 1
        else:
            O[Oi] = R[Ri]
            Ri += 1
        Oi += 1
    while Li < len(L):
        O[Oi] = L[Li]
        Li += 1
        Oi += 1
    while Ri < len(R):
        O[Oi] = R[Ri]
        Ri += 1
        Oi += 1
        
        
def SelSort(OA):
    min = 0
    for i in range(len(OA)):
        min = i
        for j in range(i+1,len(OA)):
            if OA[j]<OA[min]:
                temp = OA[min]
                OA[min] = OA[j]
                OA[j] = temp
                

def QSortLPvt(A,s,e):
    if s<e:
        pid = partL(A,s,e)
        QSortLPvt(A,s,pid-1)
        QSortLPvt(A,pid+1,e)

def partL(AR,si,ei):
    pv1 = AR[ei]
    itr = si
    pi = si
    while itr < ei and pi < ei:
        if AR[itr] < pv1:
            temp = AR[pi]
            AR[pi] = AR[itr]
            AR[itr] = temp
            itr += 1
            pi += 1
        else:
            itr += 1
    if itr == ei:
        AR[ei] = AR[pi]
        AR[pi] = pv1
    return pi

def QSortSPvt(Ar,S,E):
    if S<E:
        pind = partS(Ar,S,E)
        QSortSPvt(Ar,S,pind-1)
        QSortSPvt(Ar,pind+1,E)

def partS(AR,S,E):
    pv2 = AR[S]
    p = E
    i = E
    while i > S and p > S:
        if AR[i] > pv2:
            temp = AR[p]
            AR[p] = AR[i]
            AR[i] = temp
            i -= 1
            p -= 1
        else:
            i -= 1
    if i == S:
        AR[i] = AR[p]
        AR[p] = pv2
    return p

def BubbleSort(OA):
    tot = 0
    itr = len(OA)
    while tot < len(OA)-1:
        print("Loop:",tot)
        for i in range(0,len(OA)):
            for j in range(i+1,itr):
                if OA[j] < OA[i]:
                    temp = OA[i]
                    OA[i] = OA[j]
                    OA[j] = temp
                    print("\ti:{};j:{})Updated Array:{}".format(i,j,OA))
                    break
                else:
                    print("\ti:{};j:{})Updated Array :{}".format(i,j,OA))
                    break
        itr -= 1
        tot += 2
        print("itr:{},tot:{}".format(itr,tot))
        

OA = ['M', 'A', 'T', 'H', 'O', 'O', 'R']
print("Original Array:",OA)
MSort(OA)
print("Sorted Array with MergeSort: ",OA)
print("*********************************************************")
OA = ['A','S','H','B','U','R','N']
print("Original Array:",OA)
SelSort(OA)
print("Sorted Array with SelSort: ",OA)
print("*********************************************************")
OA = ['A','S','H','B','U','R','N']
print("Original Array:",OA)
QSortLPvt(OA,0,len(OA)-1)
print("Sorted Array with QSort - pv as last index: ",OA)
print("*********************************************************")
OA = ['A','S','H','B','U','R','N']
print("Original Array:",OA)
QSortSPvt(OA,0,len(OA)-1)
print("Sorted Array with QSort - pv as first index: ",OA)
print("*********************************************************")
OA = [2,7,4,1,5,3]
print("Original Array:",OA)
BubbleSort(OA)
print("Sorted Array with BubbleSort: ",OA)
print("*********************************************************")
