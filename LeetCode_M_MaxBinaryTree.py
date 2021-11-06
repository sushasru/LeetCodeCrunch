#Maximum Binary Tree

class Node():
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def createMaxBinaryTree(root,arr,arrlen):
    print("\narr:{},arrlen:{}".format(arr,arrlen))
    if arrlen != 0:               
        MaxAr = max(arr)
        nd = Node(MaxAr)
        idx = arr.index(MaxAr)
        print("\tMaxAr:{},idx:{}".format(MaxAr,idx))
        root = nd
        root.rchild = createMaxBinaryTree(root.rchild,arr[idx+1:],len(arr[idx+1:]))
        #printLevelOrder(root,0)
        root.lchild = createMaxBinaryTree(root.lchild,arr[:idx],len(arr[:idx]))
    return root
        
def printLevelOrder(cur_node,level):
    mq = [cur_node]
    print("length of mq:",len(mq))
    l = []
    temp = []
    while mq:        
        ans = []
        for i in mq:
            if i:
                temp.append(i.data)
                #print("Cur Node:",temp)
                if i.lchild:
                    ans.append(i.lchild)
                    #print("\t LeftChild:",i.lchild.data)
                else:
                    ans.append(None)
                if i.rchild:
                    ans.append(i.rchild)
                    #print("\t RightChild:",i.rchild.data)
                else:
                    ans.append(None)
            else:
                temp.append(None)
        #print("\n*******\n")
        for i in ans:
            if i:
                print(i.data)
##        print("\n*******\n")
        print("\tCurrent Level Order Tree:",temp) 
        #l.append(temp)
        mq = ans
    print("Level Order Tree:",temp)           



nums = [3,2,1,6,0,5]
tree = createMaxBinaryTree(None,nums,len(nums))
printLevelOrder(tree,0)
