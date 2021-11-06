def kthGrammar(n,k,cur_val,prev_val,counter):
    print("cur_value is {} @counter:{} = n:{}".format(cur_val,counter,n))
    arr = ["0"]*(n+1)
    print(arr)
    for i in range(1,n+1):
        if i > 1:
            temp = arr[i-1]
            temp.replace("0","01")
            #arr[i]=arr[i-1].replace("0","01")
            temp.replace("1","10")
            print("temp:",temp)

        



n = 4
k = 3
print("Value at row-{} and position-{} is {}".format(n,k,kthGrammar(n,k,0,0,1)))
