def combine(n,k):
    l = [n][k]
    for r in l:
        print("here")
        for c in r:
            print("herehere")
            print(r,c)


n = 4
k = 2
print("Get combination of {} numbers out of 1 to {}".format(k,n))
combine(n,k)
n = 1
k = 1
print("Get combination of {} numbers out of 1 to {}".format(k,n))
combine(n,k)

