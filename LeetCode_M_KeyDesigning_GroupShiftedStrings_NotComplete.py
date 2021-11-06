def groupStrings(strings):
    print("\nStrings:",strings)
    dictn = {}
    for st in strings:
        s_len = len(st)
        if s_len in dictn:
            dictn[s_len].append(st)
        else:
            dictn[s_len] = [st]
        print("\tDictn:",dictn)
    return list(dictn.values())


strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
print("Result:",groupStrings(strings))
print("***********************************************\n")
strings = ["a"]
print("Result:",groupStrings(strings))
