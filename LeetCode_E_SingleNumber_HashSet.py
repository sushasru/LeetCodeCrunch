def singleNumber(nums):
    hset = {}
    for n in nums:
        if n in hset:
            hset[n] += 1
        else:
            hset[n] = 1
            
    print(min(hset, key = hset.get))

singleNumber([2,2,1])
        
        
        
