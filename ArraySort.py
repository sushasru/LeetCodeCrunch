Array = [4,1,9,5,2,3]
newArray=[]
for a in range(0, len(Array)):
        var = Array[a]
        print("Var =",var)
        for b in range(0, len(Array)):
                if Array[b] not in newArray:
                        print("\t",Array[b]," not in newArray")
                        if Array[b] <= var:
                                print("\t\t",Array[b]," less than ",var)
                                var = Array[b]
        if var not in newArray:
                newArray.append(var)
                print(newArray)
                #newArray.append(Array[a])
                #print(" ",newArray)
                
