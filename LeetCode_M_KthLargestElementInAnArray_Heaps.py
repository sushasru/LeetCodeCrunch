import heapq

def findKthLargest(nums,k):
    print("\nFind {} largest element in {}\n".format(k,nums))
    nlen = len(nums)
    for i in range(nlen//2-1,-1,-1):
        minheap(nums,i,nlen)

    for i in range(nlen-1,-1,-1):
        nums[i], nums[0] = nums[0], nums[i]
        minheap(nums,0,i)
    print("\t MinHeap:",nums)

    return nums[k-1]

def minheap(nums,cur_idx,nlen):
    smallest = cur_idx

    lidx = cur_idx*2 + 1
    ridx = cur_idx*2 + 2

    if lidx >= nlen:
        lidx = None
    if ridx >= nlen:
        ridx = None

    if lidx is not None and nums[smallest] > nums[lidx]:
        smallest = lidx

    if ridx is not None and nums[smallest] > nums[ridx]:
        smallest = ridx

    if smallest != cur_idx:
        nums[cur_idx], nums[smallest] = nums[smallest], nums[cur_idx]
        minheap(nums,smallest,nlen)
    return nums


nums = [3,2,1,5,6,4]
k = 2
print("Result:",findKthLargest(nums,k))
print("*****************************************")
nums = [3,2,3,1,2,4,5,5,6]
k = 4
print("Result:",findKthLargest(nums,k))
