#string1 = "heat"
#string2 = "hit"
#minimum deletions to make the 2 strings match
#bruteforce wont work with edge case - "ab" and "ba"

str1 = "a"
str2 = "b"
str1 = "rxsqwxvofiwklxisvzdheasbczkltcjzslbovpsaqewoggxtcmjoqxsialugufydfetarflfzsskgfjnafqlqdi"
str2 = "sxolsazosiaf"
lenstr1 = len(str1)+1
lenstr2 = len(str2)+1

PrevOptns = [0] * (lenstr2)
CurOptns = [0]* (lenstr2)

print("\nstr1:{}\nstr2:{}\nops:{}\n".format(str1,str2,PrevOptns))
#oprtns = memo(ops)
#print("No of operations:",ops[len(str1)][len(str2)])

row = 0
col = 0

for i in range(0,lenstr1):
    print("\n\tCur:{},\n\tPrev:{}".format(CurOptns,PrevOptns))
    for j in range(0,lenstr2):
        if i == 0 and j == 0:
            CurOptns[j] = 0
        elif i == 0 and j != 0:
            CurOptns[j] = j            
        elif i != 0 and j == 0:
            CurOptns[j] = i
        else:
            if str1[i-1] == str2[j-1]:
                CurOptns[j] = PrevOptns[j-1]
            else:
                print("i:{},j:{}".format(i,j))
                minval = min(PrevOptns[j], CurOptns[j-1])+1
                CurOptns[j] = minval
    

    PrevOptns= CurOptns
    CurOptns = [0]*(lenstr2)


print("\n\tCur:{},\n\tPrev:{}".format(CurOptns,PrevOptns))
print("Operations Count:",PrevOptns[lenstr2-1])





                
            
