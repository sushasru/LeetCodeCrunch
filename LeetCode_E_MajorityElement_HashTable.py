#HashTable

def majorityElement(nums):
    dictn = {}
    for n in nums:
        if n in dictn:
            dictn[n] += 1
        else:
            dictn[n] = 1
    max_key = max(dictn, key = dictn.get)
    print("max_key:",max_key)
    
    print("max_val:",max(dictn.values()))


nums = [1,2,1]
majorityElement(nums)
