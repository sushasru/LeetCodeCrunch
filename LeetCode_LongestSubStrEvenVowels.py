def findTheLongestSubstring(s):
    vowdict = {"a":0,"e":0,"i":0,"o":0,"u":0}
        
    i = 0
    ptr = 0
    maxstr = ""

    while i < len(s):
        print("\ns[{}]:{}".format(i,s[i]))
        
        if s[i] in vowdict:
            vowdict[s[i]] += 1
            print("s[{}]:{} is a vowel".format(i,s[i]))
            
            if vowdict[s[i]]>2 and vowdict[s[i]]%2 != 0:
                while s[i] not in temp:
                    i += 1
                    print(i)
                vowdict[s[i]] -= 1
                ptr = i 
                print("Updated dictionary:",vowdict)
                print("ptr is now at s[{}]:{}".format(ptr,s[ptr]))
           
        temp = s[ptr:i+1]
        print("temp:",temp)
        if len(temp) > len(maxstr):
            maxstr = s[ptr:i+1]
            print("current maxstr:",maxstr)
        
        i+=1
                

 
              
              
        
##        if s[e] in vowdict:
##            print("\t{} in vowdict:".format(s[e]))
##            vowdict[s[e]] -= 1
##            e -= 1
##            tempstr = s[i-1:e]
##            print("\tupdateddict:",vowdict)
##        elif s[i] in vowdict:
##            print("\t{} in vowdict:".format(s[i]))
##            vowdict[s[i]] -= 1
##            i += 1
##            tempstr = s[i:e+1]
##            print("\tupdateddict:",vowdict)            
##        else:            
##            i += 1
##            e -= 1
##            if len(tempstr)>len(maxstr):
##                maxstr = tempstr
##                print("\tcurrent maxstr:",maxstr)
##        st += 1
            
    print("Final MaxStr:",maxstr)
    print(vowdict)






s = "eleetminicoworoep"
print("string: ",s)
findTheLongestSubstring(s)
print("**********************************")
