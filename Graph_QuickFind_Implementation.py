class QuickFind():
    def __init__(self,N):
        print("Initialize")
        self.Ar = [i for i in range(N)]
        print("Ar:",self.Ar)
        

    def union(self,parent,child):
        print("\nUnion {} and {}".format(parent,child))
        pRoot = self.find(parent)
        cRoot = self.find(child)
        print("\t\tpRoot:{},cRoot:{}".format(pRoot,cRoot))
        if pRoot != cRoot:
            for i in range(len(self.Ar)):
                if self.Ar[i] == cRoot:
                    print("\t\t\tAr[{}]:{}".format(i,self.Ar[i]))
                    self.Ar[i] = pRoot
        print("\tAr:",self.Ar)

    def find(self,child):
##        print("\tchild:{},parent:{}".format(child,self.Ar[child]))
##        if child == self.Ar[child]:
##            return self.Ar[child]
        print("\tParent of {} is {}".format(child,self.Ar[child]))
        return self.Ar[child]
        
        

    def checkconnection(self,val1,val2):
        print("\nCheck if val1:{} is connected to val2:{}".format(val1,val2))
        if val1 >= len(self.Ar) or val2 >= len(self.Ar):
            return False
        else:
            if self.find(val1) == self.find(val2):
                return True
            else:
                return False
        
        
        


n = 10
#graph => 1-2-5-6-7 3-8-9 4

QF = QuickFind(n)
QF.union(1,2)
QF.union(2,5)
QF.union(5,6)
QF.union(6,7)
QF.union(3,8)
QF.union(8,9)
print(QF.checkconnection(1, 5))  # true
print(QF.checkconnection(5, 7))  # true
print(QF.checkconnection(4, 9))  # false
QF.union(4,9)
print(QF.checkconnection(4, 9))  # true

    


