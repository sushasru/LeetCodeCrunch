num1 = "1"
num2 = "9"

i = len(num1)-1
j = len(num2)-1
m = max(i,j)

res1 = 0
res2 = 0
res3 = 0
carry = 0
sum = []

while m>=0:
    print("m:{} i:{} j:{}".format(m,i,j))
    if i>=0:
        res1 = (ord(num1[i]) - ord('0'))
        i -= 1
    else:
        res1 = 0
        
    if j>=0:
        res2 = (ord(num2[j]) - ord('0'))
        j -= 1
    else:
        res2 = 0
        
    print("\tRES1:",res1)
    print("\tRES2:",res2)
    print("\tRES3:",res3)
    res3 =  (carry + (res1 + res2))
    carry = 0
    
    print("RES3:",res3)
    if res3 >= 10 and m!=0:
        carry = 1
        res3 = res3 - 10
    else:
        carry = 0

    
    print("\nRES3:{};\tcarry:{}".format(res3,carry))
    if res3 < 10:
        sum.append(chr(ord('0') + res3 % 10))
    else:
        while True:
            sum.append(chr(ord('0') + res3 % 10))
            res3 //= 10
            if res3 == 0:
                break

    print("CurrentSum:{}".format(sum)) 
    m -= 1

   
print(''.join(reversed(sum)))
    

    
