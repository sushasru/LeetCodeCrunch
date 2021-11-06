#QuickSort with last element as pivot key
def quicksort(array,starti,endi):
    if starti<endi:
        pindex = partitionwithlastelementaspivot(array,starti,endi)
        print("\tPindex:",pindex)
        quicksort(array,starti,pindex-1)
        quicksort(array,pindex+1,endi)

def partitionwithlastelementaspivot(array,starti,endi):
    i = starti
    pindex = starti
    pivot = array[endi]
    print("\tPivot:",pivot)
    print("\t\tStarti:",starti)
    print("\t\tPindex:",pindex)
    while i<endi and pindex <endi:
        print("\t\ti:",i)
        if array[i]<=pivot:
            temp = array[pindex]
            array[pindex] = array[i]
            array[i] = temp
            pindex += 1
            i+=1
            print("\t\t\tArray",array)
        else:
            i += 1
    #print(array[i])        
    if pindex < endi:
        array[endi]=array[pindex]
        array[pindex] = pivot
    print("\t\t\t\t{}] Array:{} ".format(starti,array))
    return pindex


Array = [8,2,6,10,4,1,13,13]
#Array = [7,2,1,6,8,5,3,4]
print("UnsortedArray: ",Array)
quicksort(Array,0,len(Array)-1)
print("SortedArray: ",Array)
