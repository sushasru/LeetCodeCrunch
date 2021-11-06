#BinarySearchTree
from collections import deque
class Node():
    def __init__(self,data=None,lchild=None,rchild=None):
        self.data = data
        self.rchild = rchild
        self.lchild = lchild
        print("Initialized Node")

class BSTree():
    def __init__(self):
        self.root = None
        print("Initialized BSTree")

    def insert(self,data):
        print("\nInsert Operation\n")
        if self.root:
            print("\tInsert as a child")
            self._insert(self.root,data)
        else:
            print("\tInsert as root")
            nd = Node(data,None,None)
            self.root = nd

    def _insert(self,cur_node,data):
        if data < cur_node.data:
            print("\t\t{} > than {}".format(data,cur_node.data))
            if cur_node.lchild:
                print("\t\t\t lchild:",cur_node.lchild.data)
                print("\t\t\t left child is not empty move on")
                self._insert(cur_node.lchild,data)
            else:
                nd = Node(data,None,None)
                cur_node.lchild = nd
        else:
            print("\t\t{} < than {}".format(data,cur_node.data))
            if cur_node.rchild:
                print("\t\t\t rchild:",cur_node.rchild.data)
                print("\t\t\t rchild is not empty move on")
                self._insert(cur_node.rchild,data)
            else:
                nd = Node(data,None,None)
                cur_node.rchild = nd          
                
            

    def printTree(self,order):
        print("\n***PRINT TREE***\n")
        level = 0
        if self.root:            
            if order == "inn":
                print("\n***IN ORDER TRAVERSAL***\n")
                self.printInOrderTree(self.root,level)                
            elif order == "pre":
                print("\n***PRE ORDER TRAVERSAL***\n")
                self.printPreOrderTree(self.root,level)                
            elif order == "post":
                print("\n***POST ORDER TRAVERSAL***\n")
                self.printPostOrderTree(self.root,level)                
            else:
                print("\n***LEVEL ORDER TRAVERSAL***\n")
                self.printlevelOrderTree(self.root)

        else:
            print("\tEmpty Tree")

    def printPreOrderTree(self,cur_node,level):
        print("**0")
        if cur_node:
            print("**1")
            #print(' '*4*level+'->',str(cur_node.data))
            print(str(cur_node.data))
            print("**2")
            self.printPreOrderTree(cur_node.lchild,level+1)
            print("**3")
            self.printPreOrderTree(cur_node.rchild,level+1)
            print("**4")
##        else:
##            print("\t\tDepth of Tree - Top Down Approach:",level)

    def printInOrderTree(self,cur_node,level):
        if cur_node:
            self.printInOrderTree(cur_node.lchild,level+1)
            #print(' '*4*level+'->',str(cur_node.data))
            print(str(cur_node.data))
            self.printInOrderTree(cur_node.rchild,level+1)
##        else:
##            print("\t\tDepth of Tree:",level)

    def printPostOrderTree(self,cur_node,level):
        if cur_node:
            self.printPostOrderTree(cur_node.lchild,level+1)
            self.printPostOrderTree(cur_node.rchild,level+1)
            #print(' '*4*level+'->',str(cur_node.data))
            print(str(cur_node.data))
##        else:
##            print("\t\tDepth of Tree - Bottome Up Approach:",level)

    def printlevelOrderTree(self,cur_node):
        mq = deque()
        mq.append(cur_node)

        while mq:
            nd = mq[0]        
            print(nd.data)
            if nd.lchild:
                mq.append(nd.lchild)
            if nd.rchild:
                mq.append(nd.rchild)
            mq.popleft()

    def TreeDepth(self,Ttype):
        if self.root:
            depth = 0
            level = 0
            ans = 0
            if Ttype == 'BtmUp':
                print("BOTTOM UP APPROACH\n")
                d=self.BTMTreeDepth(self.root)
                print("Depth:",d)
            elif Ttype == 'TDwn':
                print("TOP DOWN APPROACH\n")
                print("Depth:",self.TDwnTreeDepth(self.root,depth))
        else:
            print("Empty Tree")

    def BTMTreeDepth(self,cur_node):
        #Uses Post Order traversal -> Left, Right, Root.
        if not cur_node:
            #print("End at depth -",depth)
            return 0
        l=self.BTMTreeDepth(cur_node.lchild)
        r=self.BTMTreeDepth(cur_node.rchild)
        print("\tCur_Node:{},Depth:{}".format(cur_node.data,max(l,r)+1))
        return max(l,r)+1

    
    def TDwnTreeDepth(self,cur_node,depth):
        #Use Pre Order traversal -> Root, Left, Right
        self.ans = 0
        def TDwn(cur_node,depth):
            if not cur_node.lchild and not cur_node.rchild:
                self.ans = max(self.ans,depth+1)
                print("Here Max Depth:", self.ans)
            print("\tCur_Node:{},Depth:{}".format(cur_node.data,depth))
            if cur_node.lchild: TDwn(cur_node.lchild,depth+1)
            if cur_node.rchild: TDwn(cur_node.rchild,depth+1)
        if not cur_node:
            return 0
        TDwn(cur_node,0)
        return self.ans

    def successorsearch(self,inputval):
        print("\n****SUCCESSOR SEARCH***\n")
        def searchhelper(curnode,inputval):
            if not curnode:
                return
            searchhelper(curnode.lchild,inputval)
            print("curnode:",curnode.data)
            if curnode.data > inputval and self.temp == 0:
                print("successornode is:",curnode.data)
                self.temp = curnode.data
                pass
            searchhelper(curnode.rchild,inputval)
            return self.temp
        
        if self.root:
            self.temp = 0
            print("Successor Node:",searchhelper(self.root,inputval))
        else:
            return None

    def stackinorder(self):
        print("\nInorder traversal through stack\n")
        if self.root:
            stack = []
            curnode = self.root
            while curnode.lchild:
                curnode = curnode.lchild
                stack.append(curnode)
                print("curnode.lchild:",curnode.data)
                
            root = stack.pop()
            print("root:",root.data)
            
            while curnode.rchild:
                curnode = curnode.rchild
                print("curnode.rchild:",curnode.data)
                

        else:
            return


    def searchBST(self,val):
        def recsearchBST(curnode,val):
            if not curnode:
                return
            else:
                if curnode.data == val:
                    self.printlevelOrderTree(curnode)
                    return curnode
                else:
                    return recsearchBST(curnode.lchild,val) or recsearchBST(curnode.rchild,val)
        
        def getchildofBST(curnode,val):
            if not curnode:
                return self.result

            if curnode.data == val:
                self.result.append(curnode.data)
                if curnode.lchild:
                    self.result.append(curnode.lchild.data)
                if curnode.lchild:
                    self.result.append(curnode.rchild.data)
                print(self.result)
                return self.result
            else:
                getchildofBST(curnode.rchild,val)
                getchildofBST(curnode.lchild,val)
            return self.result

        if self.root is None:
            return
        else:
            curnode = self.root
            self.result = []
            #print("Output:",getchildofBST(curnode,val))
            recsearchBST(curnode,val)


    
            
    
            
            
            
        

b = BSTree()
#print(b.root)
##b.printTree("inn")
b.insert(4)
print(b.root.data)
print(b.root.lchild)
print(b.root.rchild)
##b.printTree("inn")
b.insert(2)
##b.printTree("inn")
b.insert(1)
b.insert(3)
b.insert(7)
b.printTree("inn")
b.successorsearch(12)
b.stackinorder()
b.printTree("level")
print("*********************")
b.searchBST(2)


##b.TreeDepth("TDwn")
##b.printTree("inn")
##b.printTree("post")
##b.TreeDepth("BtmUp")

#b.printTree("level")
##print("********************************")
##c = BSTree()
##c.insert(41)
##c.insert(65)
##c.insert(50)
##c.insert(91)
##c.insert(72)
##c.insert(99)
##c.insert(20)
##c.insert(11)
##c.insert(29)
##c.insert(32)
##c.printTree("pre")
##c.printTree("inn")
##c.printTree("post")
