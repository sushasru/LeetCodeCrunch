#Binary Tree implementation
class Node():
    def __init__(self,data=None,left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.treeSize = 0
        self.isRoot = None
        print("\nInitialized Node\n")

class BTree():
    def __init__(self):
        self.root = Node()
        print("\nInitialized Tree\n")

    def insert(self,data):
        print("\nInserting {} to Tree\n".format(data))
        if self.root.data == None:            
            nd = Node(data)
            #print(nd.data)
            self.root = nd
            self.left = None
            self.right = None
            self.isRoot = 1
            nd.treeSize += 1
        else:
            self._insert(data,self.root)

    def _insert(self,data,cur_node):
        print("\tCur_Node:",cur_node.data)
        if data < cur_node.data:
            if cur_node.left == None:
                print("\t\tLeft node is none")
                cur_node.left = Node(data)
            else:
                print("\t\tRecurse as right node")
                self._insert(data,cur_node.left)
        else:
            if cur_node.right == None:
                print("\t\tRight node is none")
                cur_node.right = Node(data)
            else:
                print("\t\tRecurse as right node")
                self._insert(data,cur_node.right)
            

    def printTree(self):
        print("\nCurrent Tree\n")
        if self.root == None:
            print("\t Tree is empty")
        else:
            self._printTree(self.root,0)

    def _printTree(self,cur_node,level):
        if cur_node != None:
            self._printTree(cur_node.left,level+1)
            print(' '*4* level + '->',str(cur_node.data))  
            self._printTree(cur_node.right,level+1)

    #def _printTree(self,cur_node):
        




t = BTree()
t.insert(5)
t.printTree()
t.insert(2)
t.insert(4)

t.printTree()
t.insert(6)
t.insert(7)
t.printTree()
t.insert(1)
t.printTree()
t.insert(3)
t.printTree()

        

