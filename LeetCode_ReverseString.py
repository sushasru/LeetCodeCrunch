def revString(idx,strs):
##    for i in range(len(str)-1,-1,-1):
##        print(str[i])
    #print("\tidx:{}".format(idx))
    if idx < int(len(strs)/2):
        return
    else:
        print("len(str):{},idx:{},len(str)-idx:{}".format(len(strs),idx,len(strs)-idx-1))
        strs[len(strs)-idx-1], strs[idx] = strs[idx], strs[len(strs)-idx-1]
        print("\tstrs:",strs)     
        revString(idx-1,strs)
    


        

strs = ["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]
revString(len(strs)-1,strs)
#['a', 'm', 'a', 'n', 'a', 'P', ' ', ':', 'l', 'a', 'n', 'a', 'c', ' ', ' ', 'a', ',', 'n', 'a', 'l', 'p', ' ', 'a', ' ', ',', 'n', 'a', 'm', ' ', 'A']
#['a', 'm', 'a', 'n', 'a', 'P', ' ', ':', 'l', 'a', 'n', 'a', 'c', ' ', 'a', ' ', ',', 'n', 'a', 'l', 'p', ' ', 'a', ' ', ',', 'n', 'a', 'm', ' ', 'A']

