def containsNearbyDuplicate(nums,k):
    print("Nums:",nums)
    print("K   :",k)
    dictn1 = {}
    dictn2 = {}
    for i,n in enumerate(nums):
        if n in dictn1 and abs(dictn1[n] - i) <= k:
            print("\tDifference:",abs(dictn1[n] - i))
            return True
        else:
            dictn1[n] = i
    print("dictn1:",dictn1)
    print("dictn2:",dictn2)

    return False

    
        
    


nums = [1,2,3,1]
k = 3
print("Result:",containsNearbyDuplicate(nums,k))
print("*****************************************\n")
nums = [1,0,1,1]
k = 1
print("Result:",containsNearbyDuplicate(nums,k))
print("*****************************************\n")
nums = [1,2,3,1,2,3]
k = 2
print("Result:",containsNearbyDuplicate(nums,k))
print("*****************************************\n")
