#to convert spreadsheet column id to corresponding integer

FieldName = "ZZ"
print("FieldName:",FieldName)
i = 0
res = 0

while i < len(FieldName):
    res = res * 26 + (ord(FieldName[i]) - ord('A')) + 1
    print("\tres:",res)
    i += 1

FieldID = res
print("FieldID:",FieldID)

print("chr(65):",chr(65))
print("chr(65):",chr(65))

string = []
print("FieldID//27:",FieldID%27)
print(65+int(FieldID/27)-1)
print(chr(65 + int(FieldID/27) - 1))
string.append(chr(65 + int(FieldID/27) -1 ))

string.append(chr(65 + FieldID%27))
print(string)

##j =0
##while True:
##    print("********")
##    print(FieldID/27)
##    print(ord('A') + FieldID%26)
##    print(ord('A') + FieldID//27 - 1)
##    print("string:",chr(ord('A') + FieldID//27 - 1))
##    string.append(chr(ord('A') + FieldID//27 - 1))
##    FieldID /= 26
##    print("FieldID:",FieldID)
##    if FieldID < 26:
##        break

#print("FieldName:",''.join(reversed(string)))

    

                    
