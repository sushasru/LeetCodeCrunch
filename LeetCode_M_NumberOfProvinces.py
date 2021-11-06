#N cities - some are connected and some are not
#eg, cities - a,b,c
#a -> b -> c then city a is connected to c indirectly
#province is a dir or in-dir connected cities

#isConnected = nxn matrix
#if isConnected[i][j] = 1 then ith and jth cities are conected
#if isConnected[i][j] = 0 then ith and jth cities are not conected
#return total number of provinces
class UnionFind:
    def __init__(self,N):
        self.Ar = [i for i in range(N)]
        self.ArRank = [1 for i in range(N)]
        self.count = N

    def find(self,child):
        if child == self.Ar[child]:
            return child
        self.Ar[child] = self.find(self.Ar[child])
        return self.Ar[child]

    def union(self,parent,child):
        pRoot = self.find(parent)
        cRoot = self.find(child)

        if pRoot != cRoot:
            if self.ArRank[pRoot] > self.ArRank[cRoot]:
                self.Ar[cRoot] = pRoot
                self.ArRank[pRoot] += 1
            elif self.ArRank[pRoot] < self.ArRank[cRoot]:
                self.Ar[pRoot] = cRoot
                self.ArRank[cRoot] += 1
            else:
                self.Ar[cRoot] = pRoot
                self.ArRank[pRoot] += 1
            self.count -= 1
        print("Array:{}\nArrayRank:{},Count:{}".format(self.Ar,self.ArRank,self.count))
                

def findCircleNum(isConnected):
    leng = len(isConnected)
    if leng == 0:
        return 0
    else:
        UF = UnionFind(leng)
        for i in range(leng):
            for j in range(leng):
                if isConnected[i][j] == 1:
                    UF.union(i,j)
                    




    
    

#isConnected = [[1,1,0,0,0,0,0,1,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,0,0,1,1,0,0,0,0],[0,0,0,1,0,1,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,1,0,1,0,0,0,0,1,0],[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,1,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],[0,0,0,0,1,1,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,1,0,1,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]]
isConnected = [[1,1,1,0,1,1,1,0,0,0],[1,1,0,0,0,0,0,1,0,0],[1,0,1,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,1,0],[1,0,0,1,1,0,0,0,0,0],[1,0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,1,0,1,0],[0,1,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,1,0,1,1],[0,0,0,0,0,0,0,1,1,1]]
findCircleNum(isConnected)
print("************************")

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
findCircleNum(isConnected)
print("************************")
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
findCircleNum(isConnected)
print("************************")
##isConnected = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
##findCircleNum(isConnected)
##print("************************")

