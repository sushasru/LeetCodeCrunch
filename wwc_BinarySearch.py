#BinarySearch
import math
def binsearch(n,arr,alen):
    print("Array to search:",arr)
    si = 0
    ei = alen-1
    while si<=ei:
        m = math.ceil((si+ei)/2)
        
        if n == arr[m]:
            print("\t\tFound {} at {}".format(n,m))
            return m
        elif n < arr[m]:
            print("\t\t{} < {}".format(n,arr[m]))
            ei = m-1
        else:
            print("\t\t{} > {}".format(n,arr[m]))
            si = m+1
        print("\n si:{}, ei:{}, mid:{}".format(si,ei,m))
    return -1
        

    
    




arr = [2,4,6,8,34,56,89]
n = 89
print(binsearch(n,arr,len(arr)))
arr = "ahbgdc"
n = "b"
print(binsearch(n,arr,len(arr)))

