#Isomorphic string - 2 strings when characters in str1 can be replaced to get str2.
#all occurrences of a character must be replaced with another character while preserving the order of the character
#No 2 characters may map to the same character, but a character may map to itself

def isIsomorphic(s,t):
    sd = {}
    newstr = ""

    for i in range(len(t)):
        print("s[{}]:{};t[{}]:{}".format(i,s[i],i,t[i]))
        if s[i] not in sd and t[i] not in sd.values():
            sd[s[i]] = t[i]
        if s[i] in sd:
            newstr += sd[s[i]]
        print("\tsd:",sd)
            

    print("s:{}\nt:{}\nnew:{}".format(s,t,newstr))

    if newstr == t:
        return True
    else:
        return False
    

##    print("sd:{}\ntd:{}".format(sd,td))
##
##    if len(sd) != len(td):
##        return False
##    else:
##        return True
        
    
    


s = "egg"
t = "add"
print("Are these strings - {} and {} Isomorphic?:{}".format(s,t,isIsomorphic(s,t)))
print("***************************************************")
s = "foo"
t = "bar"
print("Are these strings - {} and {} Isomorphic?:{}".format(s,t,isIsomorphic(s,t)))
print("***************************************************")
s = "paper"
t = "title"
print("Are these strings - {} and {} Isomorphic?:{}".format(s,t,isIsomorphic(s,t)))
print("***************************************************")
s = "bbbaaaba"
t = "aaabbbba"
print("Are these strings - {} and {} Isomorphic?:{}".format(s,t,isIsomorphic(s,t)))
print("***************************************************")
s = "badc"
t = "baba"
print("Are these strings - {} and {} Isomorphic?:{}".format(s,t,isIsomorphic(s,t)))
print("***************************************************")


