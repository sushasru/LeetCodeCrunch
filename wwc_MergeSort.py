def MergeSplit(arr):
    len_arr = len(arr)
    while len_arr > 1:
        mid = int(len_arr/2)
        MergeSort(arr[:mid])
        MergeSort(arr[mid:])

def MergeSort(arr):
    print("\tCurrent Array:",arr)
    

arr = [15, 3, 9, 8, 5, 2, 7, 1, 6]
print("array to be sorted:",arr)
MergeSplit(arr)
