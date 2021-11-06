#Symmetric Binary Tree
    #option-1 - using queue 
class Node():
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

##class BSTree():
##    #def __init__(self):
##        #self.root = None
        
def insertlevelordertree(arr,root,i,n):
    if i < n:
        if arr[i] is not None:
            nd = Node(arr[i])
            root = nd
            #print("data:",root.data)

            #print("here")
            root.lchild = insertlevelordertree(arr,root.lchild,2*i+1,n)
            root.rchild = insertlevelordertree(arr,root.rchild,2*i+2,n)
    return root


def printTree(printType):
    if not root:
        print("Empty Tree")
    else:
        if printType == "PreOrder":
            printPreOrder(root,level=0)
        if printType == "LevelOrder":
            printLevelOrder(root,level=0)

def printPreOrder(cur_node,level):
    print("****0")
    #if cur_node:
    print("****1")
    print(cur_node.data)
    print("****2")
    if cur_node.lchild: printPreOrder(cur_node.lchild,level+1)
    print("****3")
    if cur_node.rchild: printPreOrder(cur_node.rchild,level+1)
    print("****4")
    if not cur_node.lchild and not cur_node.rchild:
        print("****5")
        

def printLevelOrder(cur_node,level):
    mq = [cur_node]
    l = []
    while mq:
        temp = []
        ans = []
        for i in mq:
            temp.append(i.data)
            #print("Cur Node:",temp)
            if i.lchild:
                ans.append(i.lchild)
                #print("\t LeftChild:",i.lchild.data)
            if i.rchild:
                ans.append(i.rchild)
                #print("\t RightChild:",i.rchild.data)
                
        #print("\n*******\n")
        for i in ans:            
            print(i.data)
##        print("\n*******\n")
        l.append(temp)
        mq = ans
    print("Level Order Tree:",l)

def unival(cur_node):
    ar = [cur_node]
    l = []
    count = 0
    while ar:
        temp = []
        ans = []
        for i in ar:
            temp.append(i.data)
            print("root:",i.data)
            if i.lchild:                
                ans.append(i.lchild)
                val = ans[0].data
                print("\tlchild:",val)
            if i.rchild:
                ans.append(i.rchild)
                print("\trchild:",ans[1].data)
                if val == ans[1].data:
                    count += 1
                else:
                    count -= 1
        if val==temp[0]:
            count += 1
            print("Current Count:",count)
        val = 0
        l.append(temp)
        ar =ans

            
            

def checkSymmetry(cur_left,cur_right):
    if not cur_left and not cur_right:
        return True
    else:
        if cur_left and cur_right:
            if cur_left.data == cur_right.data:
                return checkSymmetry(cur_left.lchild, cur_right.rchild) and checkSymmetry(cur_left.rchild, cur_right.lchild)
        else:
            return False

def pathSum(cur_node,targetSum):
    print("****0,TargetSum:{}".format(targetSum))
    if not cur_node:
        print("****1")
        return False    

    if not cur_node.lchild and not cur_node.rchild and cur_node.data == targetSum:
        print("*****2")
        return True

    print("****3")
    targetSum -= cur_node.data
    print("Cur_Node:{},targetSum:{}".format(cur_node.data,targetSum))
    
    print("*****4")
    return pathSum(cur_node.lchild,targetSum) or pathSum(cur_node.rchild,targetSum)


    
    
            
            
    
    
        
    
arr = [5,1,5,5,5,None,5]
n = len(arr)
root = None
root = insertlevelordertree(arr,None,0,n)
printTree("LevelOrder")
print("Is the tree symmetric?: ",checkSymmetry(root,root))
print("Count of Unival Subtree:",unival(root))

##arr = [1,2,2,3,4,4,3]
##n = len(arr)
##root = None
##root = insertlevelordertree(arr,None,0,n)
##printTree("LevelOrder")
##print("Is the tree symmetric?: ",checkSymmetry(root,root))
##
##ar2 = [1,2,2,None,3,None,3]
##n = len(ar2)
##root = None
##root = insertlevelordertree(ar2,None,0,n)
##printTree("LevelOrder")
##print("Is the tree symmetric?: ",checkSymmetry(root,root))
##
##ar3 = [5,4,8,11,None,13,4,7,2,None,None,None,1]
##cSum = 0
##targetSum = 22
##n = len(ar3)
##root = None
##root = insertlevelordertree(ar3,None,0,n)
##printTree("PreOrder")
##print("_______________________________________________")
##print("\nPathSum:",pathSum(root,targetSum))
##print("\n\n")
##if cSum != targetSum:
##    
##    pathSum(root,targetSum,cSum)
##else:
##    print("True")


