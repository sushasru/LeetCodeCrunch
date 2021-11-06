def intersection(nums1,nums2):
   d1 = {}
   d2 = {}
   lst = []
   for n in nums1:
       if n in d1:
           d1[n] += 1
       else:
            d1[n] = 1

   for n in nums2:
       if n in d1 and d1[n] != 0:
            lst.append(n)
            d1[n] -= 1
            
           
   print("List:",lst)
   return lst

    

    

   
            
            
        
    



nums1 = [1,2,2,1]
nums2 = [2,2]
print("Find Intersection of {} and {}".format(nums1,nums2))
print("Intersection is ",intersection(nums1,nums2))
print("\n**********************************************\n")
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print("Find Intersection of {} and {}".format(nums1,nums2))
print("Intersection is ",intersection(nums1,nums2))
print("\n**********************************************\n")
nums1 = [1,2,2]
nums2 = [2]
print("Find Intersection of {} and {}".format(nums1,nums2))
print("Intersection is ",intersection(nums1,nums2))
print("\n**********************************************\n")


