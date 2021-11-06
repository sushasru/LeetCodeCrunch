#BubbleSort
def bubbleSort(arr):
    n = len(arr)    
    for i in range(0,n-1):
        print("length of array:",n-1-i)
        for j in range(i,n-1-i):
            print("i:{},j{}".format(i,j))
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
            print("\tcur arr:",arr)
        print("*****************************")

        
        

arr = [29,10,14,37,14]
print("Array to sort:",arr)
print("Sorted Array:",bubbleSort(arr))
print("*****************************")
