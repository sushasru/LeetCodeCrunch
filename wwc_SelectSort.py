#Selection Sort
def selectSort(arr):
    n = len(arr)
    for i in range(0,n-1):
        minindex = i
        for j in range(i, n):
            print("\tarr[{}]:{};mini:{}".format(j,arr[j],arr[minindex]))
            if arr[j] < arr[minindex]:
                minindex = j
                #print("\t\tMini = {}, minindex = {}".format(mini,minindex))
        #print("\t\t\tarr[{}]:{};arr[{}]:{}".format(ptr,arr[ptr],minindex,arr[minindex]))
        if minindex != i:
            arr[i],arr[minindex] = arr[minindex], arr[i]
        print("cur arr:",arr)
                
        
    



arr = [7,8,5,4,9,2]
print("Array to sort:",arr)
print("Sorted Array:",selectSort(arr))
print("*****************************")
