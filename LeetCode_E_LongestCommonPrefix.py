def longestCommonPrefix(strs):
    prefix = ""
    for i in range(len(strs)):
        if prefix == "":
            prefix = strs[i]
        else:
            print("strs:",strs[i])
            prefix = set(strs[i])&set(prefix)
            print("\tPrefix:",prefix)
    if prefix != strs[0]:
        return prefix
    else:
        return ''
                     
        


strs = ["flower","flow","flight"]
print("Strings to check:",strs)
print("Longest Prefix:",longestCommonPrefix(strs))
print("***********************************")
strs = ["dog","racecar","car"]
print("Strings to check:",strs)
print("Longest Prefix:",longestCommonPrefix(strs))
