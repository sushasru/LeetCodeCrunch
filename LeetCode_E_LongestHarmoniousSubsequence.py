#LongestHarmoniousSubsequence
import sys
def findLHS(nums):    
    length = 0
    num_d = {}
    mlen = 0
    for i in nums:
        if i in num_d:
            num_d[i] += 1
        else:
            num_d[i] = 1

    for k,v in num_d.items():
        print("k:",k)
        if k-1 in num_d:
            print("\t{} and {} in {}".format(k,k-1,num_d))
            length = v + num_d[k-1]
        elif k+1 in num_d:
            print("\t{} and {} in {}".format(k,k+1,num_d))
            length = v + num_d[k+1]
        mlen = max(mlen,length)
        print("\t\tcur maxlen:",mlen)
        length = 0

    return mlen

        



nums = [1,3,2,2,5,6,3,7]
print("nums:",nums)
print(findLHS(nums))
print("----------------------------------")
nums = [1,2,3,4]
print("nums:",nums)
print(findLHS(nums))
print("----------------------------------")
nums = [1,1,1,1]
print("nums:",nums)
print(findLHS(nums))
print("----------------------------------")
