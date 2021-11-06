def search(nums,target):
    st = 0
    ed = len(nums)

    while st < ed:
        mid = (st+ed)//2

        if nums[pv] < nums[mid+1]:
            ed = 1
            print("decrement ed :",ed)
        else:
            st += mid
            print("increment st :",st)
    print("pv:{},st:{},ed:{}".format(pv,st,ed))
            

    return -1
    

nums = [4,5,6,7,0,1,2]
target = 0
print("{} is at {} in {}".format(target,search(nums,target),nums))
