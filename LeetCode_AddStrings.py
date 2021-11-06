#Add Strings

def addStrings(num1: str, num2: str) -> str:
    sum = 0
    num = []
    carry = 0
    len1 = len(num1)-1
    len2 = len(num2)-1
    print("len1:{};len2:{}".format(len1,len2))
          
    maxlen = max(len1,len2)
    if len1 > len2 or len1 == len2:
        l = len1
        s = len2
    else:
        l = len2
        s = len2
    i = maxlen
    value =0
    for j in range(l,-1,-1):
        
        for k in range(s,-1,-1):
            print("j:{},k:{}".format(j,k))
            print(((ord(num1[j]) - ord('0')) + (ord(num2[k]) - ord('0'))))
            value = carry + ((ord(num1[j]) - ord('0')) + (ord(num2[k]) - ord('0')))
            carry = 0
            
        if value >= 10:
            carry = 1
            value = value - 10
            print("value:{};carry:{}".format(value,carry))
        else:
            carry = 0
        print("value:{};carry:{}".format(value,carry))

    print("VALUE:",value)
    print("\t\tvalue",value)
    if value < 10:
        num.append(chr(ord('0') + value % 10))
    else:
        while True:
            num.append(chr(ord('0') + value % 10))
            value //= 10
            if value == 0:
                break
       # i -= 1
    
    print(''.join(reversed(num)))   



    
##    while i >= 0:
##        print("\ti:{};maxlen:{}".format(i,maxlen))
##        print("\tCarry:",carry)
##        if i < len1:
##            print("here")
##            value = carry + (ord(num1[i]) - ord('0'))
##            carry = 0
##        elif i < len2:
##            print("herehere")
##            value = carry + (ord(num2[i]) - ord('0'))
##            carry = 0
##        elif len1<=i and len2 <=i:
##            print("hereherehere")
##            print(((ord(num1[len1]) - ord('0')) + (ord(num2[len2]) - ord('0'))))
##            value = carry + ((ord(num1[len1]) - ord('0')) + (ord(num2[len2]) - ord('0')))
##            carry = 0
##        #elif len1 < 0 and len2 < 0:
##            #print("here")
##            #value = carry + value
##        else:
##            value = value
##        print("\ti:{};val:{}".format(i,value)) 
##        if value >= 10 and i>0:
##            print("hhere")
##            carry = 1
##            value = value - 10
##        else:
##            carry = 0


        

        
        
                 
       


num1= "999"
num2="11"
print("num1:{}\nnum2:{}".format(num1,num2))

addStrings(num1,num2)
