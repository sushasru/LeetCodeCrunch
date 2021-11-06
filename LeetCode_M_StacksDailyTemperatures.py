#Daily Temperatures
def dailyTemp(T):
    warmerdays = [None]*len(T)
    stck = []
    days = len(T)-1

    for i in range(days-1):
        print("\n\tday:{},temp:{}".format(i,T[i]))
        if T[i+1]>T[i]:
            warmerdays[i] = 1
        else:
            temp = 0
            stcklen = len(stck)
            j = 0
            while j<len(stck):
                print("\t\tstck[0][{}]:{}".format(j,stck[0][j]))
                if T[i] > stck[0][j]:
                    warmerdays[j] = i-j
                j += 1
                    
            
##            warmerdays[i] = temp   
            stck.append([T[i],[i]])
            
    
            
    
            
        print("\t\tCurrent T list:",warmerdays)
        print("\t\tCurrent Stack:",stck)
    return warmerdays


T = [77,54,66,63,90,94,36,90,89,87]
print("\nTemperatures to check:",T)
print("Temparature list:{}\nOutput:{}".format(T,dailyTemp(T)))
