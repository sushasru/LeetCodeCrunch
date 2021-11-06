class Node():
    def __init__(self,val,lchild,rchild):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild
        #print("Initialized node")


class Btree():
    def __init__(self):
        self.Root = None#Node(None,None,None)
        print("Initialized Root")


    def add(self,nlist):
        for i,n in enumerate(nlist):
            if self.Root is None:
                self.Root = Node(n,None,None)
                print("self.Root",self.Root.val)
            else:
                self._add(self.Root,Node(n,None,None),i)
        self.PreOrder(self.Root,0)

    def _add(self,root,node,indx):
        parent = int((indx-1)/2)
        print("\nParent:",parent)
        print("Current Parent:",root.val)
        if parent == 0:
            if root.lchild == None:
                root.lchild = node
                print("\t{} will be inserted as lchild".format(node.val))
            else:
                root.rchild = node
                print("\t{} will be inserted as rchild".format(node.val))
        else:
            if parent%2 == 1:
                print("\tparent is now:",parent)
                child = root.lchild
            else:
                child = root.rchild
            self._add(child,node,parent)

    def PreOrder(self,root,lvl):
        if root == None:
            return
        print("{}{}".format('-'*2*lvl,root.val))
        self.PreOrder(root.lchild,lvl+1)
        self.PreOrder(root.rchild,lvl+1)
            
##        if curnode == None:
##            curnode = Node(d,None,None)
##            print("\t\t{} was inserted".format(d))
##        else:
##            print("\nCurNode:",curnode.val)
##            if curnode.lchild == None:
##                print("\t{} will be inserted as lchild".format(d))
##                curnode.lchild = self._add(curnode.lchild,d)
##                #curnode = curnode.rchild
##            else:# curnode.rchild == None:               
##                curnode.rchild = self._add(curnode.rchild,d)
##                print("\t{} was inserted as rchild".format(d))
##                curnode = curnode.lchild
##        return curnode

    def insert(self,nlist):
        nlen = len(nlist)
        if nlen != 0:
            nde = self.Root
            n = 0
            while n < nlen:
                print("nde:",nde.val)
                nd = Node(nlist[n],None,None)
                if self.Root.val == None:
                    nde = nd
                    self.Root = nde
                    print("\tInsert at Root nlist[{}]:{}".format(n,nlist[n]))
                    nde = self.Root
                elif nde.lchild == None:
                    nde.lchild = nd
                    print("\t\t{} was inserted as the lchild".format(nlist[n]))                    
                else:
                    nde.rchild = nd
                    print("\t\t{} was inserted as the rchild".format(nlist[n]))
                    nde = nde.lchild
                    
        else:
            return 
            
    
    def _insert(self, d, cur_node):
        print("\tInsert ",d)
        if cur_node.lchild == None:
            print("\t\t{} was inserted as the lchild".format(d))
            cur_node.lchild = Node(d,None,None)
            
        else:
            cur_node.rchild = Node(d,None,None)

            
    def printTree(self):
        if self.Root.val == None:
            return None
        else:
            self._printTree(self.Root,0)


    def _printTree(self,curnode,level):
        if curnode != None:
            print(str(curnode.val))
            self._printTree(curnode.lchild,level+1)            
            self._printTree(curnode.rchild,level+1)

    def leafnodeSum(self):
        if self.Root.val == None:
            return
        else:
            def _leafnodeSum(curnode):        
                if curnode == None:
                    return
                #print("Here:\t{}\n{}\t\t{}".format(curnode.val,curnode.lchild,curnode.rchild))
                if curnode.lchild == None and curnode.rchild == None and curnode.val != None:
                    self.s += curnode.val
                    print(curnode.val)
                    #return curnode.val
            
                _leafnodeSum(curnode.lchild)
                _leafnodeSum(curnode.rchild)
            
            self.s = 0
            _leafnodeSum(self.Root)
            print("Sum:",self.s)

    
        
        
                    
                    

    



Bt = Btree()
lst = [1,2,3,4,5,None,6,7,None,None,None,None,8]
##lst = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]
Bt.add(lst)
Bt.printTree()
print("**************************")
Bt.leafnodeSum()
T = []
for i,l in enumerate(lst):
    prnt = l



root = [6,7,8,2,7,1,3,9,None,1,4,None,None,None,5]


    
