

print("'a':{} to 'z':{}".format(ord('a'),ord('z')))
print("'A':{} to 'Z':{}".format(ord('A'),ord('Z')))
print("'0':{} to '9':{}".format(ord('0'),ord('9')))
print(ord('S'))

print(ord('s'))
print(chr(97))

for i in range(0,301):
    print("{}:{}".format(i,chr(i)),end=" ")
    if i == 100:
        print("\n")
    elif i == 200:
        print("\n")

print("\n")
lowr = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for l in lowr:
    print("{}:{}".format(l,ord(l)),end=" ")
print("\n")
for u in upper:
    print("{}:{}".format(u,ord(u)),end=" ")

    
