def containsNearbyDuplicate(nums,k):
    print("\nList:",nums)
    dictn = {}
    for i,val in enumerate(nums):
        if val in dictn:
            if abs(dictn[val]-i) <= k:
                print("i:{} and j:{}".format(dictn[val],i))
                print("True!")
                return True
            else:
                dictn[val] = i
        else:
            dictn[val] = i
        print("\tcurrent dictn:",dictn)
    return False


nums = [1,2,3,1]
k = 3
containsNearbyDuplicate(nums,k)
print("**************************")
nums = [1,0,1,1]
k = 1
containsNearbyDuplicate(nums,k)
print("**************************")
nums = [1,2,3,1,2,3]
k =2
containsNearbyDuplicate(nums,k)
print("**************************")
