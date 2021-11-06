class QuickUnionByRank:
    def __init__(self,N):
        self.Ar = [i for i in range(N)]
        self.ArRank = [1 for i in range(N)]
        print("Initial Array:{}\nArray Rank   :{}".format(self.Ar,self.ArRank))


    def find(self,child):
        print("\tParent of {} is {}".format(child,self.Ar[child]))
        if child == self.Ar[child]:
            return child
        self.Ar[child] = self.find(self.Ar[child])
        return self.Ar[child]
    
    def unionByRank(self,parent,child):
        print("\nUnion {} and {}".format(parent,child))
        pRoot = self.find(parent)
        print("\t\tpRoot:{}".format(pRoot))
        cRoot = self.find(child)
        print("\t\tcRoot:{}".format(cRoot))
        if pRoot != cRoot:
            if self.ArRank[pRoot] > self.ArRank[cRoot]:
                self.Ar[cRoot] = pRoot
                self.ArRank[pRoot] += 1
            elif self.ArRank[pRoot] < self.ArRank[cRoot]:
                self.Ar[pRoot] = cRoot
                self.ArRank[cRoot] += 1
            else:
                print("herE")
                self.Ar[cRoot] = pRoot
                self.ArRank[pRoot] += 1
        print("\n\t\tArray        :{}\n\t\tArray Rank   :{}".format(self.Ar,self.ArRank))

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

QU = QuickUnionByRank(n)
QU.unionByRank(1,2)
QU.unionByRank(2,5)
QU.unionByRank(5,6)
QU.unionByRank(6,7)
QU.unionByRank(3,8)
QU.unionByRank(8,9)
print(QU.checkconnection(1,5))
print(QU.checkconnection(5,7))
print(QU.checkconnection(4,9))
QU.unionByRank(9,4)
print(QU.checkconnection(4,9))
print(QU.checkconnection(1,3))
QU.unionByRank(1,3)
print(QU.checkconnection(1,3))

