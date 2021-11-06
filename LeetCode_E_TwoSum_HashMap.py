def twoSum(nums,target):
    dictn = {}
    numcheck = 0

    for i,n in enumerate(nums):
        numcheck = target-n
        if numcheck in dictn:
            print(dictn[numcheck],i)
            return(dictn[numcheck],i)
        else:
            dictn[nums[i]]=i
        print("\tcur dictn:",dictn)
    return 0
        


nums = [2,7,11,15]
target = 9
print("Output:",twoSum(nums,target))
print("**************************************")
nums = [3,2,4]
target = 6
print("Output:",twoSum(nums,target))
print("**************************************")
nums = [3,3]
target = 6
print("Output:",twoSum(nums,target))

