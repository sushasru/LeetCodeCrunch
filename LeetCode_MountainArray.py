def validMountainArray(arr):
    if len(arr) < 3:
        print("\tError! Not a valid array to check")
        return False
    else:
        eindex = len(arr)-1
        sindex = 0
        mid = int(len(arr)/2)
        while sindex < mid and eindex > mid:
            print("\t\tsindex: {}, mid: {}, eindex: {}".format(sindex,mid,eindex))
            if arr[sindex] < arr[sindex+1]:
                print("\t\t\tarr[{}] < arr[{}] - move forward!".format(sindex, sindex+1))
                if arr[eindex] < arr[eindex-1]:
                    print("\t\t\tarr[{}] < arr[{}] - move forward!".format(eindex, eindex-1))
                    #if arr[sindex] < arr[mid] and arr[mid] > arr[eindex]:
                    eindex -= 1
                    sindex += 1
                    #else:
                        #print("{} is not a mountain array!".format(arr))
                        #return False
                else:
                    print("\t\t\tError! arr[{}] is not less than arr[{}]".format(eindex, eindex-1))
                    print("\t{} is not a mountain array!".format(arr))
                    return False
            else:
                print("\t\t\tError! arr[{}] is not less than arr[{}]".format(sindex, sindex+1))
                print("\t{} is not a mountain array!".format(arr))
                return False
        print("\t{} is a valid mountain array!".format(arr))
        return True
            


arr = [2,1]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [3,5,5]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [1,3,2]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [0,3,2,1]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [0,2,3,4,5,2,1,0]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [0,2,3,3,5,2,1,0]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [0,1,2,3,4,8,9,10,11,12,11]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
