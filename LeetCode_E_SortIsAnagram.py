def MSort(st,st1):
    stlen = len(st)
    print(stlen)
    if stlen > 1:
        mid = int(stlen/2)
        print("\tMid:",mid)
        print("\tArray-LA:",st[:mid])
        LA = MSort(st[:mid],st1)
        print("\t\tLA:",LA)
        print("\tArray:",st[mid:])
        RA = MSort(st[mid:],st1)
        print("\t\tRA:",RA)
        MSortMerge(LA,RA,st1)

def MSortMerge(LA,RA,st1):
    print("Compare {} with {} and update {}".format(LA,RA,st1))
    Li = 0
    Ri = 0
    si = 0
    Llen = len(LA)
    Rlen = len(RA)
    Slen = len(st1)

    while Li < Llen and Ri < Rlen:
        if LA[Li] < RA[Ri]:
            si += 1
            st1 = LA[Li]+st1[si:]
            Li += 1
        else:
            si += 1
            st1 = RA[Ri]+st1[si:]
            Ri += 1
        print("\tUpdated String:",st)

    while Li < Llen:
        si += 1
        st1 = LA[Li] + st1[si:]
        Li += 1
    while Ri < Rlen:
        si += 1
        st1 = RA[Ri] + st1[si:]
        Ri += 1
        

def isAnagram(s,t):
    slen = len(s)
    tlen = len(t)
    if slen != tlen:
        return False
    else:
        print(MSort(s,s))
        print(MSort(t,t))




s = "anagram"
t = "nagaram"
print("Is {} an anagram of {}?".format(s,t))
print("Result:",isAnagram(s,t))
print("************************************\n")
