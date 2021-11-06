def intersection(nums1,nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    if len(set1)<len(set2):
        setintersection(set1,set2)
    else:
        setintersection(set2,set1)


def setintersection(set1,set2):
    new = [x for x in set1 if x in set2]
    print(new)


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
intersection(nums1,nums2)

nums1 = [1,2,2,1]
nums2 = [2,2]
intersection(nums1,nums2)

