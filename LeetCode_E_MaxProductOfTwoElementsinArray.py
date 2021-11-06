import heapq

def maxProduct(nums):
    print("\nNums:",nums)

    #Sort - TC - O(nlogn)
##    MSort(nums)
##    print("\tSorted Array:",nums)
##    print("Result:",(nums[0]-1)*(nums[1]-1))

    
    #Heap - TC - O(nlogn)
    nlen = len(nums)
    for i in range(nlen//2-1,-1,-1):
        MinHeap(nums,i,nlen)

    
    for i in range(nlen-1,-1,-1):
        nums[i],nums[0] = nums[0],nums[i]
        MinHeap(nums,0,i)

    print("heap:",nums)
    print("Result:",(nums[0]-1)*(nums[1]-1))


        
    
def MinHeap(nums,cur_idx,nlen):
    smallest = cur_idx
    prnt_idx = -(cur_idx//-2)-1
    l_idx = cur_idx * 2 + 1
    r_idx = cur_idx * 1 + 1

    if prnt_idx <= 0:
        prnt_idx = None
    if l_idx >= nlen:
        l_idx = None
    if r_idx >= nlen:
        r_idx = None

    if l_idx is not None and nums[smallest]>nums[l_idx]:
        smallest = l_idx

    if r_idx is not None and nums[smallest]>nums[r_idx]:
        smallest = r_idx

    if smallest != cur_idx:
        nums[smallest], nums[cur_idx] = nums[cur_idx], nums[smallest]
        MinHeap(nums,smallest,nlen)

def MSort(nums):
    nlen = len(nums)
    if nlen > 1:
        mid = int(nlen/2)
        left = MSort(nums[:mid])
        right = MSort(nums[mid:])
        Merge(left,right,nums)
    return nums

def Merge(left,right,nums):
    li = 0
    ri = 0
    ni = 0

    llen = len(left)
    rlen = len(right)
    nlen = len(nums)

    while li < llen and ri < rlen:
        if left[li] > right[ri]:
            nums[ni] = left[li]
            ni += 1
            li += 1
        else:
            nums[ni] = right[ri]
            ni += 1
            ri += 1

    while li<llen:
        nums[ni] = left[li]
        ni += 1
        li += 1
    while ri<rlen:
        nums[ni] = right[ri]
        ni += 1
        ri += 1

    return nums

nums = [3,4,5,2]
maxProduct(nums)
print("****************************************")
nums = [1,5,4,5]
maxProduct(nums)
print("****************************************")
nums = [3,7]
maxProduct(nums)
print("****************************************")
