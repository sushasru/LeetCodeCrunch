def LongestPalindrome(s):
    s_d = {}
    for i in s:
        if i not in s_d:
            s_d[i] = 1
        else:
            s_d[i] += 1
    print(max(s_d.values()))
    print(s_d)
    itr = 0
    odd = 0
    palindrome = 0
    for k,v in s_d.items():
        print(k,v)
        if v%2 == 0:
            palindrome += v
            print("\tpalindrome:",palindrome)
            print("\tv:",k)
        else:
            if v < 2:
                print("\todd:",odd)
                if odd == 0:
                    odd = 1
                    palindrome += 1
                    print("\tpalindrome:",palindrome)
                    print("\tv:",k)
            else:
                palindrome += v-1
                print("\tpalindrome:",palindrome)
                print("\tv:",k)
                    
        
##    while itr < len(s_d):
##        if s_d[s[itr]]%2 == 0:
##            palindrome += s_d[s[itr]]
##        else:
##            if s_d[s[itr]] < 2:
##                if odd == 0:
##                    odd = 1
##                    palindrome += 1
##            else:
##                palindrome += (s_d[s[itr]]-1)
##        itr += 1
    print("Length of longest string:",palindrome)
    return palindrome

    
s = "abcCccdd"
print(s)
op = LongestPalindrome(s)
print("---------------------------------------")
s = "a"
print(s)
op = LongestPalindrome(s)
print("---------------------------------------")
s = "ccc"
print(s)
op = LongestPalindrome(s)
