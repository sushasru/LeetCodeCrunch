#number of good pairs
def numIdenticalPairs(nums):
    num_d = {}
    count = 0
    f= 0
    for n in nums:
        if n in num_d:
            num_d[n] += 1
        else:
            num_d[n] = 1

    for k,v in num_d.items():
        print("{}:{}".format(k,v))
        if v >= 2:
            f = v*(v-1)#goodPairCount(v)
            f = f//2
##            print("{}! = {}".format(v,f))
##            print("{}/2:{}".format(f,f//2))
##            print("{}/2:{}".format(v,v//2))
##            print("2*{}:{}".format(v//2, 2*(v//2)))
            count += f
            print("cur count:",count)
    return count 


def goodPairCount(v):
    
    if v == 0:
        print("\t0")
        return 0
    elif v == 1:
        print("\t1")
        return 1
    else:
        print("\tv:",v)
        return v*goodPairCount(v-1)




nums = [1,2,3,1,1,3]
print("Nums:",nums)
print("Identical Pairs in the array:",numIdenticalPairs(nums))
print("********************************************************")
nums = [1,1,1,1]
print("Nums:",nums)
print("Identical Pairs in the array:",numIdenticalPairs(nums))
print("********************************************************")
nums = [1,2,3]
print("Nums:",nums)
print("Identical Pairs in the array:",numIdenticalPairs(nums))
print("********************************************************")

