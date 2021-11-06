#QSort - All methods
def QSort2Ptr(a,si,ei):
    if si<ei:
        pv = getSPV2ptr(a,si,ei)
        QSort2Ptr(a,si,pv-1)
        QSort2Ptr(a,pv+1,ei)
    return a

def getLPV2ptr(a,si,ei):
    print("\n\tGet PV from {} when pval = {}".format(a[si:ei+1],a[ei]))
    pval = a[ei]
    li = si
    ui = ei
    while li < ui:
        if a[li]>pval:
            if a[ui]<pval:
                a[ui], a[li] = a[li], a[ui]
            else:
                ui -= 1
        else:
            li += 1
    a[ei], a[ui] = a[ui], a[ei]
    print("\t\tSorted Array:{}, PV is {}".format(a[si:ei+1],ui))
    return ui

def getSPV2ptr(a,si,ei):
    print("\n\tGet PV from {} when pvak = {}".format(a[si:ei+1],a[si]))
    pval = a[si]
    li = si
    ui = ei
    while li < ui:
        while a[li]<=pval and li<ei:
            li += 1
        while a[ui] > pval and ui>si:
            ui -= 1
        if li<ui:
            a[li], a[ui] = a[ui], a[li]
        li += 1
    a[si], a[ui] = a[ui], a[si]
    print("\t\tSorted Array:{}, PV is {}".format(a[si:ei+1],ui))
    return ui

def QSort1Ptr(a,si,ei):
    if si < ei:
        pv = getSPV1ptr(a,si,ei)
        QSort1Ptr(a,si,pv-1)
        QSort1Ptr(a,pv+1,ei)
    return a

def getLPV1ptr(a,si,ei):
    print("\n\tGet PV from {} when pval is {}".format(a[si:ei+1],a[ei]))
    pval = a[ei]
    li = si
    p = si
    while li<ei:
        if a[li] < pval:
            if li != p:
                a[li], a[p] = a[p], a[li]
            li += 1
            p += 1
        else:
            li += 1
    a[ei], a[p] = a[p], a[ei]
    print("\t\tSorted Array:{}, PV is {}".format(a[si:ei+1], p))
    return p 

def getSPV1ptr(a,si,ei):#???????
    print("\n\tGet PV from {} when pval is {}".format(a[si:ei+1],a[ei]))
    pval = a[si]
    li = si
    p = si
    while li<ei:
        if a[li] <= pval:
            if li != p:
                a[li], a[p] = a[p], a[li]
            li += 1
            p += 1
        else:
            li += 1
    a[si], a[p] = a[p], a[si]
    print("\t\tSorted Array:{}, PV is {}".format(a[si:ei+1], p))
    return p 
   
a=[3, 44, 38, 5, 37, 15, 36, 27, 2, 46, 4, 19, 50, 48]
print("Array to sort:",a)
print("SortedArray:",QSort2Ptr(a,0,len(a)-1))
a=[3, 44, 38, 5, 37, 15, 36, 27, 2, 46, 4, 19, 50, 48]
print("Array to sort:",a)
print("SortedArray:",QSort1Ptr(a,0,len(a)-1))
