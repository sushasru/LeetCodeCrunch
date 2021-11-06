def removeDuplicates(S):
    st = []
    newstr = ''
    slen = len(S)
    for i in range(slen):
        print("Cur String:",S[i])
        if len(st) == 0:
            st.append(S[i])
            newstr += st[-1]
        else:
            if st[-1] == S[i]:
                st.pop()
                print("\t1.Current stack:{}, String:{}".format(st,S[:len(st)]))
                newstr = S[:len(st)]
            else:
                st.append(S[i])
                newstr += st[-1]
                print("\t2.Current stack:{}, String:{}".format(st,newstr))
    print("\t3.Current stack:{}, String:{}".format("".join(st),newstr))
    return st


S = "abbaca"
removeDuplicates(S)
