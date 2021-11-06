def maxheapitr(ar):
    print("Initial ar:",ar)
    for i in range(len(ar)):
        curnode = ar[i]
        lchildindx = 2*i+1
        rchildindx = 2*i+2
        
        if i != 0:
            parent = ar[-(i//-2)-1]
        else:
            parent = curnode

        if 2*i+1 < len(ar):
            lchild = ar[2*i+1]
        else:
            lchild = None

        if 2*i+2 < len(ar):
            rchild = ar[2*i+2]
        else:
            rchild = None

        print("cur node is {}\nparent of cur node is {}\n\tlchild of curnode is {}\n\trchild of curnode is {}\n".format(ar[i],parent,lchild,rchild))

        if rchild is not None:
            if lchild is not None and lchild < rchild:
                if curnode < rchild:
                    print("\t\tSwap curnode with rchild")
                    ar[i], ar[rchildindx] = ar[rchildindx], ar[i]
        
        if lchild is not None:
            if rchild is not None and lchild > rchild:
                if curnode < lchild:
                    print("\t\tSwap curnode with lchild\n")
                    ar[i], ar[lchildindx] = ar[lchildindx], ar[i]

        print("{} - Updated Array:{}\n".format(i,ar))
    return ar
                

def maxheaprec(ar,i):
    print("{} - Array:{}".format(i,ar))     
    largest = i
    curnode = ar[i]
    if i!=0:
        parent = ar[-(i//-2)-1]
    else:
        parent = curnode
        
    lchildidx = 2*i+1
    rchildidx = 2*i+2
    arlen = len(ar)
    
    print("cur node is {}\nparent of cur node is {}\n".format(ar[i],parent))

    if lchildidx < arlen:
        if rchildidx < arlen:
            if ar[lchildidx] > ar[i]:
                largest = lchildidx
            else:
                largest = i

            if ar[largest] < ar[rchildidx]:
                largest = rchildidx
            print("\tlchild of curnode is {}\n\trchild of curnode is {}\n".format(ar[lchildidx],ar[rchildidx]))
            print("\tlargestidx:{}, i:{}".format(largest,i))
            if largest != i:
                print("\t\tswap!")
                ar[i], ar[largest] = ar[largest], ar[i]
                maxheaprec(ar,largest)
            else:
                i = len(ar)//2 - 1
                print("\t\tnext")
                maxheaprec(ar,i+1)
            
        else:
            rchildidx = None
    else:
        lchildidx = None

    return ar

def leaves(ar):
    arlen = len(ar)
    rangeofleaves = arlen//2
    return ar[rangeofleaves:arlen]

def heapnodes(ar):
    arlen = len(ar)
    rangeofnodes = arlen//2
    return ar[:rangeofnodes]
    
    
    

    
        
        
    
            
        
##ar = [1,14,10,8,7,9,3,2,4,6]
##maxheap = maxheapitr(ar)
##print("\nIterative max heap of {} is {}".format(ar,maxheap))
##print("\nLeaves in heap:",leaves(ar))
##print("\nNodes in heap:",heapnodes(ar))
##print("***************************************************************\n")
##ar = [14,1,10,8,7,9,3,2,4,6]
##maxheap = maxheaprec(ar,0)
##print("\nRecursive max heap of {} is {}".format(ar,maxheap))
##print("\nLeaves in heap:",leaves(ar))
##print("\nNodes in heap:",heapnodes(ar))
##print("***************************************************************\n")
##ar = [3,6,5,0,8,2,19,9]
##maxheap = maxheaprec(ar,0)
##print("\nRecursive max heap of {} is {}\n".format(ar,maxheap))
##maxheap = maxheapitr(ar)
##nodeheap = maxheapitr(heapnodes(maxheap))
##leavesheap = maxheapitr(leaves(maxheap))
##print("\nLeaves in heap:",nodeheap + leavesheap)
##print("\nIterative max heap of {} is {}".format(ar,leaves(maxheap)))
##print("***************************************************************\n")
ar = [2,15,4,30,18,6,25]
maxheap = maxheaprec(ar,len(ar)//2 - 1 )
print("\nRecursive max heap of {} is {}".format(ar,maxheap))
print("\nLeaves in heap:",leaves(ar))
print("\nNodes in heap:",heapnodes(ar))

