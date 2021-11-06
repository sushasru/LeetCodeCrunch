def repeatedNTimes(A):
    if len(A) % 2 != 0 :
        print("Odd length Array")
    else:
        print("here")
        dict = {}
        for i in range(0,len(A)):
            print("i:{},A[{}]:{}".format(i,i,A[i]))
            if A[i] not in dict:
                dict[A[i]] = 1
                print("dictionary: ",dict)
            else:
                dict[A[i]] += 1
                print("dictionary updated: ", dict)
                if dict[A[i]] == len(A)/2:
                    print("Repeating element is {}".format(A[i]))
                    return A[i]

A = [1,2,3,3]
repeatedNTimes(A)
