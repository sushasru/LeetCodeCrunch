#MedianOf2SortedArrays
def findMedianSortedArrays(nums1, nums2):
    for i in range(0,len(nums1)):
        binsearch(nums2,nums1[i])
    print("Num:{}".format(num))

def binsearch(nums2,n):
        mid = int(len(nums2)/2)
        for i in range(0,len(nums2)):
            if nums2[mid] == n:
                
nums1 = [1,3]
nums2 = [2]
print("nums1: {}, nums2:{}".format(nums1,nums2))
median = findMedianSortedArrays(nums1,nums2)
print("Median:{}".format(median))
