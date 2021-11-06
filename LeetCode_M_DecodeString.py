def decodeString(s):
    slen = len(s)
    i = 0
    result = ""
    temp = ""
    while i < slen-1:
        print(s[i])
        if s[i] == '[':
            n = int(s[i-1])
            i += 1
            print("\tn:",n)
            while s[i] != ']' or s[i] != ']':
                temp += s[i]
                i+= 1
                print("\t\ttemp:",temp)
            result += n*temp
            temp = ""
            print("result:",result)
        else:
            i += 1
    


s = "3[a]2[bc]"
decodeString(s)
print("****************")
s = "3[a2[c]]"
decodeString(s)
print("****************")
