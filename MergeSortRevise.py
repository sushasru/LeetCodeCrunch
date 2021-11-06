def MSplit(ar):
    ar_len = len(ar)
    print("\nMSplitndSort\n\tCurrent Array Length:",ar_len)
    if ar_len >1:
        mid = int(ar_len/2)
        LA = ar[:mid]
        RA = ar[mid:]
        print("\tLeft Array:",LA)
        print("\tRight Array:",RA)
        MSplit(LA)
        MSplit(RA)
        MSortndMerge(LA,RA,ar)
    return ar

def MSortndMerge(LA,RA,ar):
    print("\nSort and Merge Arrays")
    Li =0
    Ri =0
    Ai =0
    L_len = len(LA)
    R_len = len(RA)
    
    print("\n\tCompare LA:{} & RA:{} and update ar:{}".format(LA,RA,ar))
    while Li < L_len and Ri < R_len:
        print("\tcurrent index: Li-{}, Ri-{}, Ai-{}".format(Li,Ri,Ai))
        if LA[Li] <= RA[Ri]:
            ar[Ai] = LA[Li]
            Li += 1
        else:
            ar[Ai] = RA[Ri]
            Ri += 1
        Ai += 1
    while Li < L_len:
        ar[Ai] = LA[Li]
        Ai += 1
        Li += 1
    while Ri < R_len:
        ar[Ai] = RA[Ri]
        Ai += 1
        Ri += 1
    print("\tcurrent Arr:",ar)
            






ar = [3,44,38,5,37,15,36,27,2,46,4,19,50,48]
print("Array to sort:", ar)
print("Sorted Array:",MSplit(ar))
print("*******************************************")
