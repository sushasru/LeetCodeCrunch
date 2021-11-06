def firstUniqChar(s):
    dictn = {}
    for c in s:
        if c not in dictn:
            dictn[c] = 1
        else:
            dictn[c] += 1
    print(dictn)
    lst = list([keys for keys,values in dictn.items() if values == 1])
    if len(lst) > 0:
        return s.index(lst[0])
    else:
        return -1
    


s = "leetcode"
print("\nFirst non-repeating character in {} is {}".format(s,firstUniqChar(s)))
print("**************************************************\n")
s = "susha"
print("\nFirst non-repeating character in {} is {}".format(s,firstUniqChar(s)))
print("**************************************************\n")
s = "avinash"
print("\nFirst non-repeating character in {} is {}".format(s,firstUniqChar(s)))
print("**************************************************\n")
s = "mathoor"
print("\nFirst non-repeating character in {} is {}".format(s,firstUniqChar(s)))
print("**************************************************\n")
s = "aabba"
print("\nFirst non-repeating character in {} is {}".format(s,firstUniqChar(s)))
print("**************************************************\n")
s = "aadadaad"
print("\nFirst non-repeating character in {} is {}".format(s,firstUniqChar(s)))
print("**************************************************\n")

