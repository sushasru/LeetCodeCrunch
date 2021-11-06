import sys
def lengthOfLongestSubstring(s:str) -> int:
    maxlen = -sys.maxsize - 1
    if len(s) >= 1:
        ptr1 = 0
        ptr2 = 0
        print("\tptr1:{}, ptr2:{}".format(s[ptr1],s[ptr2]))
        dictn = {}
        for i in range(len(s)):
            print("\t\ts[{}]:{}".format(i,s[i]))
            print("\t\tptr1:{}, ptr2:{}".format(s[ptr1],s[ptr2]))
            if s[i].lower() not in dictn.keys():
                dictn[s[i].lower()] = i
                ptr2 += 1
                if len(dictn) > maxlen:
                    maxlen = len(dictn)
            else:
                print("\n\t\t***s[{}]:{} in dictn - {}\n".format(i, s[i], dictn))
                print("\t\t\tdictn[s[{}]]:{}".format(i,dictn[s[i]]))
                j =0
                
                while (j<ptr2) and (s[i].lower() in dictn.keys()):
                    print("j:{},ptr1:{},ptr2:{}".format(j,ptr1,ptr2))
                    print(list(dictn.keys())[ptr1])
                    dictn.pop(list(dictn.keys())[ptr1],None)
                    #print("\t\t\t",s[j])
                    
                    #dictn.pop(s[j].lower(),None)
                    print("\t\t\tPoppedDictionary:",dictn)
                    j += 1 
                    print("**ptr1:{}",j)
                    
                
                dictn[s[i].lower()] = i
                ptr1 = dictn[s[i]] + 1
            print("\n\t\tCurrent Elements in dictn:",dictn)
            print("\t--------------------------------------")
        return maxlen
    else:
        return 0
            

s="qrsvbspk"
print("String:",s)
print("LongestSubstring:",lengthOfLongestSubstring(s))    

##s="Russia"
##print("String:",s)
##print("LongestSubstring:",lengthOfLongestSubstring(s))
##
s="Mathematics"
print("String:",s)
print("LongestSubstring:",lengthOfLongestSubstring(s))

##s="bbbbb"
##print("\nString:",s)
##print("LongestSubstring:",lengthOfLongestSubstring(s))
##
##s="pwwkew"
##print("\nString:",s)
##print("LongestSubstring:",lengthOfLongestSubstring(s))
##
##s=" "
##print("\nString:",s)
##print("LongestSubstring:",lengthOfLongestSubstring(s))
##
##s="abcabcbb"
##print("\nString:",s)
##print("LongestSubstring:",lengthOfLongestSubstring(s))
##
##
