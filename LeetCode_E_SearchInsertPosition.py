#Search Insert Position
def searchInsert(nums,target):
    nlen = len(nums)
    if nlen != 0:
        st_idx = 0
        end_idx = nlen-1
        while st_idx <= end_idx:
            mid = (st_idx+end_idx)//2
            if nums[mid] == target:
                print("{} is at index {}".format(target,mid))
                return mid
            elif nums[mid] < target:
                st_idx = mid+1
            else:
                end_idx = mid-1
        print("st_idx:{},mid:{},end_idx:{}".format(st_idx,mid,end_idx))
        print("{} can be inserted at index {}".format(target,st_idx))
        return st_idx
                
            
    


nums = [1]
target = 2
print("Find position of {} in {}".format(target,nums))
searchInsert(nums,target)
