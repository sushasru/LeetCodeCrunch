#Insertion Sort
def insertSort(arr):
    n = len(arr)
    j = 1
    movptr = 1
    sortedptr2 = 1
    for i in range(sortedptr2,n,1):
        print("\ti: {}) arr[{}]:{}".format(i,i,arr[i]))
        movptr = i
        for j in range(movptr,0,-1):
            print("\t\tj: {}) arr[{}]:{}".format(j,j,arr[j]))
            print("\t\t\tIs arr[{}]:{}>arr[{}]:{}?".format(j-1,arr[j-1],movptr,arr[movptr]))
            if arr[j-1]>arr[movptr]:
                print("\t\t\t\tYES! SWAP! ")
                arr[j-1], arr[movptr] = arr[movptr], arr[j-1]
                print("\t\t\t\t\tUpdated arr:",arr)
                movptr -= 1
                #print("\t\t\t\t\tmovptr:",movptr)
            else:
                print("\tNO! Dont Swap! Move ptr to next in array")
                sortedptr2 += 1
                break
                print("Sortedptr:",sortedptr2)
    return arr


arr = [14,33,27,10,35,19,42,44]
print("Array to sort:",arr)
print("Sorted Array:",insertSort(arr))
print("*****************************")
arr = [7,8,5,4,9,2]
print("Array to sort:",arr)
print("Sorted Array:",insertSort(arr))
print("*****************************")
