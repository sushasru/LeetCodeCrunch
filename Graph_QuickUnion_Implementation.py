class QuickUnion():
    def __init__(self,N):
        print("Initialize")
        self.Ar = [i for i in range(N)]
        print("\tInitial Ar:",self.Ar)

    def union(self,parent,child):
        print("\nUnion {} and {}".format(parent,child))
        pRoot = self.find(parent)
        print("\t\tpRoot:{}".format(pRoot))
        cRoot = self.find(child)
        print("\t\tcRoot:{}".format(cRoot))
        if pRoot != cRoot:
            self.Ar[child] = pRoot
        print("\tAr:",self.Ar)

    def find(self,child):
        print("\tchild:{},parent:{}".format(child,self.Ar[child]))
        if child == self.Ar[child]:
            return child
        self.Ar[child] = self.find(self.Ar[child])        
        return self.Ar[child]

    def checkconnection(self,val1,val2):
        lenAr = len(self.Ar)
        print("\nCheck if val1:{} is connected to val2:{}".format(val1,val2))
        if val1 >= lenAr or val2 >= lenAr:
            return False
        else:
            if self.find(val1) == self.find(val2):
                return True
            else:
                return False



n = 10
#graph => 1->2->5->6->7 3->8->9 4

QU = QuickUnion(n)
QU.union(1,2)
QU.union(2,5)
QU.union(5,6)
QU.union(6,7)
QU.union(3,8)
QU.union(8,9)
print(QU.checkconnection(1,5))
print(QU.checkconnection(5,7))
print(QU.checkconnection(4,9))
QU.union(9,4)
print(QU.checkconnection(4,9))
QU.union(1,4)
print(QU.checkconnection(1,4))
        
        
    
