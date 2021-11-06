#Min Number of steps to Make 2 Strings Anagram
def anag(s,t):
    if len(s) != len(t):
        return "Strings are of different lengths! Cannot be Anagrams!"
    else:
        MoveCount = 0
        i = 0
        dictnry1 = {}
        dictnry2 = {}
        for i in range(0,len(s)):
            if s[i] in dictnry1:
                dictnry1[s[i]] += 1
            else:
                dictnry1[s[i]] = 1

        for i in range(0,len(t)):
            if t[i] in dictnry2:
                dictnry2[t[i]] += 1
            else:
                dictnry2[t[i]] = 1

        i = 0
        while i < len(dictnry1):
            print("\t Is {} in {}?".format(t[i],dictnry1))
            if t[i] not in dictnry1:
                print("\t\t No!")
                MoveCount += 1
            else:
                print("\t\t Yes!")
                if dictnry2[t[i]] > dictnry1[t[i]]:
                    MoveCount += 1
                    dictnry2[t[i]] -= 1
##                elif dictnry2[t[i]] < dictnry1[t[i]]:
##                    dictnry1[t[i]] -= 1
##                else:                    
##                    dictnry1[t[i]] -= 1
##                    dictnry
                print("\t\tcur dictnry1:{},\n\t\tdictnry2:{}".format(dictnry1,dictnry2))
            i += 1
            print("cur movecount:",MoveCount)
    return MoveCount

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
print("******************************")
s = "anagram"
t = "mangaar"
print("string1:",s)
print("string2:",t)
maxMoveCount = anag(s,t)
print("MaxMoveCount:",maxMoveCount)
print("******************************")
s = "xxyyzz"
t = "xxyyzz"
print("string1:",s)
print("string2:",t)
maxMoveCount = anag(s,t)
print("MaxMoveCount:",maxMoveCount)
print("******************************")
s = "friend"
t = "family"
print("string1:",s)
print("string2:",t)
maxMoveCount = anag(s,t)
print("MaxMoveCount:",maxMoveCount)
