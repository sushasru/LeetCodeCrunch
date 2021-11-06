def isValid(s):
    par_count = 0
    sq_count = 0
    br_count = 0
    brktOpen = False
    slen = len(s)
    for i in range(slen):
        print("\tChecking ",s[i])
        if s[i] == "(":
            if brktOpen == False:
                par_count += 1
                brktOpen = True
            else:
                return False
        elif s[i] == ")":
            if par_count == -1:
                return False
            else:
                par_count -= 1
                brktOpen = False
        elif s[i] == "{":
            if brktOpen == False:
                br_count += 1
                brktOpen = True
            else:
                return False
        elif s[i] == "}":
            if br_count == -1:
                return False                
            else:
                br_count -= 1
                brktOpen = False
        elif s[i] == "[":
            if brktOpen == False:
                sq_count += 1
                brktOpen = True
        elif s[i] == "]":
            if sq_count == -1:
                return False
            else:
                sq_count -= 1
                brktOpen = False
        print("\t\t\tar_count:{},br_count:{},sq_count:{}".format(par_count,br_count,sq_count))
    if par_count == 0 and br_count == 0 and sq_count == 0:
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
