hset = set()
hset.add(3)
hset.add(2)
hset.add(1)
print("hset:",hset)
hset.add(2)
if 2 in hset:
    print("2 is in hset")
print("hset[0]:",hset[0])







def containsDuplicate(nums):
    print("len(nums):",len(nums))
    print("len(set(nums)):",len(set(nums)))
    dictn = set()
    for n in nums:
        print("checking ",n)
        if n in dictn:
            return True
        else:
            dictn.add(n)
    return False
    
nums = [1,1,1,3,3,4,3,2,4,2]
print("Does {} have duplicates?:{}".format(nums,containsDuplicate(nums)))
