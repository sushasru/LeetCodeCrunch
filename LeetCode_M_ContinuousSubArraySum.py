#Check SubArray Sum
def checkSubArraySum(nums,k):
    minsize = 1
    ptr = 0
    cur_sum = 0
    i = 0
    array_flag = False
    while i < len(nums)-1:
        print("nums[ptr]:{}; nums[i]:{}".format(nums[ptr],nums[i+1]))
        cur_sum += nums[ptr] + nums[i+1]
        print("\t Cur_Sum:",cur_sum)
        if cur_sum%k != 0:
            print("\t\t not divisible by {}".format(k))
            ptr += 1
            cur_sum = 0
        else:
            print("\t\t divisible by {}".format(k))
            minsize += (i-ptr)+1
            print("\t\t array size:",minsize)
            if minsize >= 2:
                array_flag = True
        i += 1
        
    if minsize >= 2 and cur_sum != 0:
        return array_flag
    else:
        return array_flag
    
            
        



nums = [23,2,4,6,7]
k = 6
print("nums:{}; k:{}".format(nums,k))
print("Result:",checkSubArraySum(nums,k))
print("********************************************")
nums = [23,2,6,4,7]
k = 6
print("nums:{}; k:{}".format(nums,k))
print("Result:",checkSubArraySum(nums,k))
print("********************************************")
