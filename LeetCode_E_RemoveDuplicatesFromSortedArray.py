def removeDuplicates(nums):
    print("\nArray to check:",nums)
    lptr = 0
    rptr = lptr + 1
    nlen = len(nums)
    while lptr < nlen and rptr < nlen:
        print("\tnums[{}]:{};nums[{}]:{}".format(lptr,nums[lptr],rptr,nums[rptr]))
        if nums[lptr] == nums[rptr]:
            nums[rptr] = '-'
            rptr += 1
        else:
            lptr += 1
            print("\t\tnums[{}]:{};nums[{}]:{}".format(lptr,nums[lptr],rptr,nums[rptr]))
            nums[lptr] = nums[rptr]
            print("\t\tCurrent Array:",nums)
            if lptr != rptr:
                nums[rptr] = '-'
            rptr += 1
        print("\tcurrent lptr:",lptr)
        print("\tCurrent Array:",nums)
            
        

##nums = [1,1,2]
##removeDuplicates(nums)
##print("******************************************")
##nums = [0,0,1,1,1,2,2,3,3,4]
##removeDuplicates(nums)
##print("******************************************")
nums = [1,2]
removeDuplicates(nums)
