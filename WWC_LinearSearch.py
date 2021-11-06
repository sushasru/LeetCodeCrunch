def linearr(arr,n):
    for i in range(0,len(arr)-1):
        print("{}:{}".format(i,arr[i]))
        if arr[i] == n:
            print("Found {} at Ar[{}]".format(arr[i],i))
            return True
        

arr = [2,4,6,8,34,56,89]
n = 34
linearr(arr,n)
