#Min Number of steps to Make 2 Strings Anagram
def anag(s,t):
    sDict = {}
    for i in range(0,len(s)):
        if s[i] not in sDict:
            sDict[s[i]] = 1
        else:
            sDict[s[i]] += 1
    keys = list(sDict.keys())
    values = list(sDict.values())
    print("\n\tsDictionary:",sDict)
    #print("sDictionary values:",sDict.values())
    print("\tsDictionary Max val:",max(sDict.values()))
    j = 0
    movecount = 0 
    while j < len(t) or max(sDict.values()) > 0:
        print("\n\tj:",j)
        print("\t\tIs {} in {}?".format(t[j],sDict))
        if t[j] in sDict:
            sDict[t[j]] -= 1
            print("\t\tcur sDict:",sDict)
            if sDict[t[j]] == -1:
                print("\t\t\there")
                #print(t[0:j-1])
                #print(t[len(t)-j+1:])
                print("\t\t\tReplace t[{}]:{} with {}".format(j,t[j],max(sDict,key=sDict.get)))
                t = t.replace(t[j],max(sDict,key=sDict.get),1)
                movecount += 1
                print("\t\t\tMoveCount:",movecount)
                sDict[max(sDict,key=sDict.get)] -= 1
                print("new str:",t)
                
        else:
            print("\t\t\therehere")
            print("\t\t\tReplace t[{}]:{} with {}".format(j,t[j],max(sDict,key=sDict.get)))
            t = t.replace(t[j],max(sDict,key=sDict.get),1)
            movecount += 1
            print("new str:",t)
            
            sDict[max(sDict,key=sDict.get)] -= 1
        print("sDictionary Max val:",max(sDict.values()))
        j+=1
    print("New string:",t)
    return movecount
        

s = "bab"
t = "aba"
print("string1:",s)
print("string2:",t)
maxMoveCount = anag(s,t)
print("MaxMoveCount:",maxMoveCount)
print("******************************")
s = "leetcode"
t = "practice"
print("string1:",s)
print("string2:",t)
maxMoveCount = anag(s,t)
print("MaxMoveCount:",maxMoveCount)
