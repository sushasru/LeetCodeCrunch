values = ["a","c","d","b","c","s"]

print(values)
notbindex = 0
i = 0
length = len(values)
acount = 0

while i < length:
    print("values[{}]:{}".format(i,values[i]))
    if values[i] != "b":
        values[notbindex] = values[i]
        print("\tNotBvalues[{}]:{}".format(notbindex,values[i]))
        notbindex += 1
    if values[i] == "a":
        acount += 1
    print(values)
    i += 1

print("notbindex:{}; acount: {}".format(notbindex,acount))
print("*****************************")
#values[:] = values[:notbindex]

print(values)
j = notbindex - 1
notbindex += acount - 1 
final_size = notbindex + 1

print("\nj:{}; notbindex:{}; ".format(j,notbindex))
while j >= 0:
    print(values[j])
    if values[j] == "a":
        values[notbindex-1:notbindex+1] = "dd"
        notbindex -= 2
    else:
        values[notbindex] = values[j]
        notbindex -= 1
    print(values)
    j -= 1
          
print("Values:",values)
