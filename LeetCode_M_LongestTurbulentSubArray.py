#Longest Turbulent SubArray
def lenofmaxturb(arr):
    s_id = 0
    grtr = False
    lesr = True
    ar_len, max_len = 0, 0
    i = 0
    k = 0
    if len(arr) == 1:
        return 1
    else:
        while i < len(arr)-1:
            k = i+1
            print("\narr[{}]:{},arr[{}]:{}".format(i,arr[i],k,arr[k]))
            if arr[k] < arr[i] and arr[i] > arr[:
                if(ar_len <= 8):
                    print("\tarr[{}]:{} < arr[{}]:{}".format(i,arr[i],k,arr[k]))
                
                lesr = True
                grtr = False
                #print("\t\tincrement length, cur len:",ar_len)
            elif arr[i] > arr[k] and grtr == False:
                if(ar_len <= 8):
                    print("\tarr[{}]:{} > arr[{}]:{}".format(i,arr[i],k,arr[k]))
                grtr = True
                lesr = False
                
                #print("\t\tincrement length, cur len:",ar_len)
            elif arr[i] == arr[k]:
                s_id = k
                
            else:
                if i == 0:
                    s_id = i+1
                else:
                    s_id = i
                grtr = False
                lesr = False
                #print("\t\tdecrement length, cur len:",ar_len)
                
            print("\tpointer is at arr[{}]:{} ".format(s_id,arr[s_id]))
            ar_len = (k-s_id)+1
            if ar_len >= 1:
                print("cur subarray:",arr[s_id:k+1])
            print("\tcur ar_len:",ar_len)
            print("\tcur grtr:{},lesr:{}".format(grtr,lesr))   
            max_len = max(ar_len,max_len)
            i += 1
    return max_len
        





##arr = [9,4,2,10,7,8,8,1,9]
##print("arr:",arr)
##print(lenofmaxturb(arr))
##print("------------------------------------------")
##arr = [4,8,12,16]
##print("arr:",arr)
##print(lenofmaxturb(arr))
##print("------------------------------------------")
##arr = [100]
##print("arr:",arr)
##print(lenofmaxturb(arr))
##print("------------------------------------------")
##arr = [0,1,1,0,1,0,1,1,0,0]
##print("arr:",arr)
##print(lenofmaxturb(arr))
print("------------------------------------------")
arr = [8,8,9,10,6,8,2,4,2,2,10,6,6,10,10,2,3,5,1,2,10,4,2,0,9,4,9,3,0,6,3,2,3,10,10,6,4,6,4,4,2,5,1,4,1,1,9,8,9,5,3,5,5,4,5,5,6,5,3,3,7,2,0,10,9,7,7,3,5,1,0,9,6,3,1,3,4,4,3,6,3,2,1,4,10,2,3,4,4,3,6,7,6,2,1,7,0,6,8,10]
print("arr:",arr)
print(lenofmaxturb(arr))
