#SORTING

#1. QUICKSORT - O(nlogn)
#select a pivot element
#find the best position for the pivot element in the array
#the best position is where all the elements before the pivot are less than the pivot
#and all the elements after the pivot are greater than the pivot
#do inplace sort recursively to sort the sub array elements before the pivot and elements after the pivot values
def QSort(OArray,st_index, en_index):
    if st_index < en_index:
        newpv_index = Partition(OArray,st_index,en_index)
        print("newpv_index:",newpv_index)
        print("en_index:",en_index)
        if newpv_index < en_index:
            QSort(OArray,st_index,newpv_index-1)
            QSort(OArray,newpv_index+1,en_index)


def Partition(OArray,st_index,en_index):
    itr = st_index
    pv_idx = st_index
    pv_value = OArray[en_index]
    
    print("\nPivot Value: ",pv_value)
    while itr < en_index and pv_idx < en_index:
        if OArray[itr]<pv_value:
            print("itr:",itr)
            print("pv_idx:",pv_idx,"\n****")
            temp = OArray[itr]            
            OArray[itr] = OArray[pv_idx]
            OArray[pv_idx] = temp
            pv_idx += 1
            itr += 1
            print("\tUpdated Array: ",OArray)            
        else:
            print("itr:",itr,"\n****")
            itr += 1
    if itr == en_index:
        print("pv_idx:",pv_idx,"\n****")
        OArray[en_index] = OArray[pv_idx]
        print("\t\tPivoting in progress:",OArray)
        OArray[pv_idx] = pv_value
    print("\t\tPivoted Array:",OArray)
    return pv_idx

#2. SELECTIONSORT
#Compare each element in array to find the min element
#Min element will set as the first element
#Repeat comparison until end of array
#Big O - O(n^2)
def SELECTSORT(Arr):
    for i in range(len(Arr)):
        min = i
        for j in range(i+1,len(Arr)):
            if Arr[j]<Arr[min]:
                min = j

        temp = Arr[min]
        Arr[min] = Arr[i]
        Arr[i] = temp
        print("\t {})Sorting in progress : {}".format(i,Arr))

#3. MERGESORT
#Split array into halves until there are only one element per array
#Sort and merge each array - 2 at first
#Sort and merge until all small arrays are tied togther
def MergeSort(Arr):
    n = len(Arr)
    #print("Array: ",Arr)
    #print("Array Length: ",n)
    if len(Arr)>1:
        mid = n//2
        #print("Array Mid Point: ",mid)
        L_Arr = []
        R_Arr = []
        for i in range(0,mid):
            #print("\titr_i:",i)
            L_Arr.append(Arr[i])
        for j in range(mid,n):
            #print("\titr_j:",j)
            R_Arr.append(Arr[j])
    
        print("\t\t {} \t {}".format(L_Arr,R_Arr))
        
        MergeSort(L_Arr)
        MergeSort(R_Arr)
        print("********************************")
        Sort(L_Arr,R_Arr,Arr)


def Sort(L_Arr,R_Arr,Arr):
    n_L = len(L_Arr)
    n_R = len(R_Arr)
    counter = 0
    i = 0
    j = 0
    k = 0
    while i < n_L and j < n_R:
        if L_Arr[i] <= R_Arr[j]:
            Arr[k]=L_Arr[i]
            #print("i-{}) Array: {}".format(i,Arr))
            i += 1
        else:
            Arr[k]=R_Arr[j]
            #print("j-{}) Array: {}".format(j,Arr))
            j += 1
        k += 1
        print("k-{}) Array: {}".format(k,Arr))
    while i < n_L:
        Arr[k] = L_Arr[i]
        #print("k-{}) Array: {}".format(k,Arr))
        i += 1
        k += 1
    while j < n_R:
        Arr[k] = R_Arr[j]
        #print("k-{}) Array: {}".format(k,Arr))
        j += 1
        k += 1
    print("k-{}) Array: {}".format(k,Arr))
        

       
        
            
    


#OrigArray = [8,4,1,10,3,7,5,1]
OrigArray = [9,4,8,6]
print("Original Array: ",OrigArray)    
QSort(OrigArray,0,len(OrigArray)-1)
print("Sorted Array via QuickSort: ",OrigArray)
#OrigArray = [9,4,8,6]
#print("Original Array: ",OrigArray)
#SELECTSORT(OrigArray)
#print("Sorted Array via SelectSort: ",OrigArray)
OrigArray = [2,4,1,6,8,5,3,7]
print("Original Array: ",OrigArray)
MergeSort(OrigArray)
print("Sorted Array: ",OrigArray)
