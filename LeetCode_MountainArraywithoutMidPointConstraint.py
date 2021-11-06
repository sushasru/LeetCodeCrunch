def validMountainArray(arr):
    if len(arr) < 3:
        print("\tError! Not a valid array to check")
        return False
##    elif len(arr) == 3:
##        if arr[0] < arr[1]:
##            if arr[1] > arr[2]:
##                print("\t{} is a valid mountain array!".format(arr))
##                return True
##            else:
##                print("\t{} is not a mountain array!".format(arr))
##                return False
##        else:
##            print("\t{} is not a mountain array!".format(arr))
##            return False
    else:
        index = 0
        direction = "up"
        while index < len(arr)-1:
            print("\t\tindex: {}".format(index))
            print("\t\t\tCompare arr[{}]:{} with arr[{}]:{}".format(index,arr[index], index+1,arr[index+1]))
            if arr[0] < arr[1]:
                if arr[index]<arr[index+1]:
                    if direction == "up":
                        print("direction:^")
                        print("\t\t\tarr[{}]:{} < arr[{}]:{} - move forward!".format(index,arr[index], index+1,arr[index+1]))
                        index += 1
                        direction = "up"
                    else:
                        print("\t{} is not a mountain array!".format(arr))
                        return False
                else:
                    if index < len(arr) and arr[index] > arr[index-1]:
                        print("direction:v")
                        print("\t\t\tarr[{}]:{} < arr[{}]:{} - move forward!".format(index+1,arr[index+1], index,arr[index]))
                        index += 1
                        direction = "down"
                    else:
                        print("\t{} is not a mountain array!".format(arr))
                        return False
            else:
                print("\t{} is not a mountain array!".format(arr))
                return False
                
        print("direction:",direction)
        print("length:",len(arr)-1)
        if direction == "up":
            print("\t{} is not a mountain array!".format(arr))
            return False
        else:
            print("\t{} is a valid mountain array!".format(arr))
            return True
            
        
                
            
                      


arr = [2,0,2]
print("Array to check : ",arr)
validMountainArray(arr)
#print("*****************************")
#arr = [3,5,5]
#print("Array to check : ",arr)
#validMountainArray(arr)
print("*****************************")
arr = [1,3,2]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
#arr = [0,3,2,1]
#print("Array to check : ",arr)
#validMountainArray(arr)
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
arr = [0,1,2,3,4,8,9]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [9,8,7,6,5,4,3,2,1,0]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
arr = [0,1,2,1,2]
print("Array to check : ",arr)
validMountainArray(arr)
print("*****************************")
