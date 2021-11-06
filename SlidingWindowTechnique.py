#Sliding window technique
#Fixed Window approach
#Find Max sum of a contiguous subarray of size 3
import sys

def GetMaxSum(Ar,k):
    ArSum = 0
    MaxSoFar = -sys.maxsize-1
    for i in range(len(Ar)):
        ArSum += Ar[i]
        print("\t{}:{}; ArSum->{}".format(i,Ar[i],ArSum))
        if i>=k-1:
            MaxSoFar = max(MaxSoFar,ArSum)
            print("\t\tMaxSoFar:",MaxSoFar)
            print("Ar[{}]:{}".format(i-(k-1),Ar[i-(k-1)]))
            ArSum -= Ar[i-(k-1)]
    return MaxSoFar
            

Ar = [4,2,1,7,8,1,2,8,1,0]
k = 3
print("Array: {}, Size of SubArray: {}".format(Ar,k))
print("Max sum :",GetMaxSum(Ar,k))
