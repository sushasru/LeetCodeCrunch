#Longest Repeating character replacement
def charreplace(s,k):
    max_len, st_ptr, s_len, i = 0, 0, 0, 0

    while i < len(s)-1:
        print("{}-s[{}]:{}".format(i,i,s[i]))
        if s[i] != s[i+1] and k > 0:
            print("\there\n\ts[{}]:{}, s[{}]:{}".format(i,s[i],i+1,s[i+1]))
            print(s[i:i+1+1])
            print(s[i])
            print(s[i+1+1:])
            s = s[i:i+1+1]+s[i]+s[i+1+1:]
            k -= 1
        elif s[i] != s[i+1] and k == 0:
            print("\therehere\n\ts[{}]:{}, s[{}]:{}".format(i,s[i],i+1,s[i+1]))            
            st_ptr = i+1

            
        s_len = (i+1-st_ptr)+1
        max_len = max(s_len,max_len)
        print("\t\tcur string:",s)
        print("\t\tcur len:",s_len)
           

        i += 1
    

    return max_len



s = "ABAB"
k = 2
print("Replace {} characters in {} to get longest substring".format(k,s))
print(charreplace(s,k))
print("-----------------------------------------------------------------")
s = "AABABBA"
k = 1
print("Replace {} characters in {} to get longest substring".format(k,s))
print(charreplace(s,k))
print("-----------------------------------------------------------------")
