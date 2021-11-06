def shuffle(nums,n):
    i = 1
    temp = 0
    mid = n
    while i < n:
        print("i:{}".format(i))
        print("n:{}, nums[{}]:{}".format(mid,mid,nums[mid]))
        print("\tswap mid nums[{}]:{} with nums[{}]:{}".format(mid,nums[mid],i,nums[i]))
        temp = nums[i]
        nums[i] = nums[mid]
        if i == 3:
            mid += 1
        
        nums[mid] = temp
        
        print("\t\tcurrent array:",nums)
        i += 1
        
    print("Final Array:",nums)
    return nums
        
        



nums = [7,5,9,7,5,8,10,4,3,3,2,5,9,10]
n = 7
print("Array:",nums)
print("mid point:",n)
shuffle(nums,n)
print("***********************************************")
#[7,4,5,3,9,3,7,2,5,5,8,9,10,10]
nums = [2,5,1,3,4,7]
n = 3
print("Array:",nums)
print("mid point:",n)
shuffle(nums,n)

nums = [1,2,3,4,4,3,2,1]
n = 4
print("Array:",nums)
print("mid point:",n)
shuffle(nums,n)
