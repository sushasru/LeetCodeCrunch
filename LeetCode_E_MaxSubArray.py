def maxSubArray(nums):
    maxSum = -10^5
    st_idx = 0
    e_idx = 0
    tempsum = 0
    nlen = len(nums)
    while st_idx < nlen and e_idx < nlen:
        print("st_idx:{},e_idx:{}".format(st_idx,e_idx))
        tempsum += nums[e_idx]
        print("\ttempsum =",tempsum)
        if maxSum < tempsum:
            print("\t{}<{}".format(maxSum,tempsum))
            maxSum = tempsum           
            
        else:
            tempsum = nums[e_idx]
            st_idx = e_idx
            maxSum = tempsum

        e_idx += 1
            

        
    return maxSum
    
    

nums = [-2,1,-3,4,-1,2,1,-5,4]
print("maxSubArraySum of {} is {}".format(nums,maxSubArray(nums)))

##stidx= 0;e_idx = 1
##-2,1
##    tempsum = -2+1 = -1
##    -1 > min
##        stidx += 1
##        e_idx += 1 
##
##stidx = 1, e_idx= 2
##1,-3
##    tempsum = -1+(-3) = -4
##    -4 < -1
##        tempsum = -3
##        st_idx = 2
##        maxsum = -3
##
##
##stidx = 2, e_idx = 3
##-3,4
##    tempsum = -3 + 4 = 1
##    1 > -3
##    stodx += 1
##    eidx += 1
##
##stidx = 
    
##stidx = 1
##-2+1
##    -1 > 2
##    stidx += 1
##
##stidx = 2
##-1+-4
##    -4 <-1
##
##stidx = 2
