#3Sum
'''
nums[i] + nums[left] + nums[right] = 0
'''

#BruteForce
def BFthreesum(nums):
    print("Initial Nums:",nums)
    newarr = []
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                if nums[i]+nums[j]+nums[k] == 0:
                    lst = [nums[i],nums[j],nums[k]]
                    if lst not in newarr:
                        newarr.append(lst)
            print(newarr)
                    

#2Pointers
#O(n^2)
'''
if target < 0: left ++
    target > 0: right ++
    target == 0: left ++, rigth -= 1

while left<right and nums[left] == nums[left-1]: left ++ to avoid duplicate elements in the source array
while left<right and nums[right] == nums[right-1]: left ++ to avoid duplicate elements in the source array


'''
def slidingThreeSum(nums):
    print("Initial Nums:",nums)
    itr = 0    
    nums.sort()
    print("Sorted Nums :",nums)
    nlen = len(nums)
    result = []
    while itr < nlen:
        lptr = itr+1
        rptr = itr+2
        print("iptr:{},lptr:{},rptr:{}".format(itr,lptr,rptr))
        while lptr < rptr and rptr < nlen:
            print("\tnums[{}]:{},nums[{}]:{},nums[{}]:{}".format(itr,nums[itr],lptr,nums[lptr],rptr,nums[rptr]))
            if nums[itr] + nums[lptr] + nums[rptr] == 0:
                if [nums[itr],nums[lptr],nums[rptr]] not in result:
                    result.append([nums[itr],nums[lptr],nums[rptr]])
                rptr += 1
            elif nums[itr] + nums[lptr] + nums[rptr] > 0:
                lptr += 1
            else:
                rptr += 1
            print("\t\tcur result:",result)
        
        itr += 1
        
    


nums =  [-1,0,1,2,-1,-4]
slidingThreeSum(nums)
nums =  []
nums =  [0]
