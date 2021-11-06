class Graph:
    def __init__(self,size):
        self.size = size
        self.gph = [[] for i in range(size)]
        print("\nInitialized Graph of size ",self.size)

    
    def bfs(self,pts,s,end):
        print("\nBFS {} from {} to {}".format(pts,s,end))
        for i,e in pts:
            if e not in self.gph[i]:
                self.gph[i].append(e)
            if i not in self.gph[e]:
                self.gph[e].append(i)
                
        print("\nGPH:",self.gph)
        prev = self.solve(g,s,n)
        print("\nPrev:",prev)
        return self.reconstructedpath(s,end,prev)

    def solve(self,g,s,n):
        q = []
        q.append(s)
        v = [False for i in range(n)]
        v[s] = True    
        prev = [None for i in range(n)]
        

        while q:
            node = q.pop(0)           
            print("\tCur Node:",node)
            neigh = self.gph[node]
            print("\t\tNeighbors:",neigh)
            for nxt in neigh:
                if v[nxt] == False:
                    q.append(nxt)
                    v[nxt] = True
                    prev[nxt] = node
                    print("\t\tCur Q:{}\n\t\tCur V:{}\n\t\tCur Prev:{}".format(q,v,prev))
        return prev
            
            
        

    def reconstructedpath(self,s,end,prev):
        path = []
        at = prev[end]
        while at is not None:
            print("at:",at)
            path.append(at)
            at = prev[at]
            print("\tCurrent Path:",path)
            
        path.reverse()
        
        if path[0] == s:
            print("\nPath is ",path)
        else:
            print("\nPath is None")


n = 13
g = Graph(n)

pts = [[10,1],[10,9],[10,1],[1,8],[9,8],[9,0],[8,12],[0,7],[0,11],[12,2],[11,7],[7,6],[7,3],[2,3],[3,4],[6,5]]
start = 0
end = 12
g.bfs(pts,start,end)
