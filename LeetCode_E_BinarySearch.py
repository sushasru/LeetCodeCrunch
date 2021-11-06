#BinarySearch-Easy
def search(nums,target):
    nlen = len(nums)
    if nlen != 0:
        st_idx = 0
        end_idx = nlen-1
        while st_idx <= end_idx:
            mid = (st_idx+end_idx)//2
            print("st_idx:{},mid:{},end_idx:{}".format(st_idx,mid,end_idx))
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                st_idx = mid+1
            else:
                end_idx = mid-1
        return -1 

def firstBadVersion              
            
            
nums = [5]
target = 5
print("Is {} in {}?{}".format(target,nums,search(nums,target)))
