#IsSubsequence
import math
       
def isSubsequence(s,t):
    s_idx = 0
    t_idx = 0
    prev_idx = -1
    slen = len(s)
    tlen = len(t)
    
    while s_idx < slen and t_idx < tlen:
        matched = False
        print("\ts_idx:{},t_idx:{}".format(s_idx,t_idx))
        if s[s_idx] == t[t_idx]:
            print("\t\tFound {} at {} in {}".format(s[s_idx],t_idx, t))
            
            
            if t_idx > prev_idx:
                prev_idx = t_idx
                matched = True
                s_idx += 1
                t_idx += 1
            else:
                return False
        else:
            print("\t\tMove to next character in {}".format(t))
            t_idx += 1
            
               
    if matched == False:
        return False
    else:
        if s_idx < t_idx and s_idx < slen:
            return False
        else:
            return True
        
        
        
            

    

s = "abc"
t = "ahbgdc"
print("\nIs {} subsequence of {}?".format(s,t))
print("\nResult: ",isSubsequence(s,t))
print("\n**********************************************\n")
s = "axc"
t = "ahbgdc"
print("\nIs {} subsequence of {}?".format(s,t))
print("\nResult: ",isSubsequence(s,t))
print("\n**********************************************\n")
s="acb"
t="ahbgdc"
print("\nIs {} subsequence of {}?".format(s,t))
print("\nResult: ",isSubsequence(s,t))
print("\n**********************************************\n")
