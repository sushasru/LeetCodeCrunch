def groupAnagrams(strs):
    dictn = {}
    
    print("\nStrings:",strs)
    for s in strs:        
        lst = []
        tup = ()
        for c in s:
            lst.append(c)
        lst.sort()
        tup = tuple(lst)
        print("\tList:",lst)
        if tup in dictn:
            dictn[tup].append(s)
        else:
            dictn[tup] = [s]
        print("\tdictn:",dictn)
    return list(dictn.values())
        
                


strs=["eat","tea","tan","ate","nat","bat"]
print("Result:",groupAnagrams(strs))
print("*****************************************************")
strs = [""]
print("Result:",groupAnagrams(strs))
print("*****************************************************")
strs = ["a"]
print("Result:",groupAnagrams(strs))
print("*****************************************************")
strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
print("Result:",groupAnagrams(strs))
