def isValid(s):
    st = []
##    for i in range(len(s)):
##        if len(st) == 0:
##            if s[i] == ")" or s[i] == "}" or s[i] == "]":
##                return False
##            else:
##                st.append(s[i])
##                print("\tCurrent stack:",st)
##        else:
##            if st[-1] == "(" and s[i] == ")":
##                st.pop()
##                print("\tStack after pop:",st)
##            elif st[-1] == "{" and s[i] == "}":
##                st.pop()
##                print("\tStack after pop:",st)
##            elif st[-1] == "[" and s[i] == "]":
##                st.pop()
##                print("\tStack after pop:",st)
##            else:
##                st.append(s[i])
##                print("\tStack after append:",st)
##    print("Final Stack:",st)
    par_dictn = {"(":")","{":"}","[":"]"}
    print(par_dictn.values())
##    for i in s:
##        if s[i] in  par_dictn
            
    if len(st) == 0:
        return True
    else:
        return False
            
            
        


s = "()"
print("Is {} valid? {}".format(s,isValid(s)))
print("*****************************************\n")
s = "()[]{}"
print("Is {} valid? {}".format(s,isValid(s)))
print("*****************************************\n")
s = "(]"
print("Is {} valid? {}".format(s,isValid(s)))
print("*****************************************\n")
s = "([)]"
print("Is {} valid? {}".format(s,isValid(s)))
print("*****************************************\n")
s = "{[]}"
print("Is {} valid? {}".format(s,isValid(s)))
print("*****************************************\n")
