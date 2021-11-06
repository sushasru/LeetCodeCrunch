#bidirectional graph with n vertices -> 0 to n-1 (inclusive)
#input - 2D integer array edges[i] = [ui,vi]; ui and vi are the connected vertices
#every vertex pair is connected by atmost one edge, no vertex has an edge to itself
#Determin if path exists from vertex start to vertex end
#return true if valid path exists
class graph:
    def __init__(self, N):
        self.Ar = [i for i in range(N)]
        print("Initial Array:",self.Ar)

    def find(self,child):
        if child == self.Ar[child]:
            return child
        self.Ar[child] = self.find(self.Ar[child])
        return self.Ar[child]

    def union(self,parent,child):
        print("\nUnion {} and {}".format(parent,child))
        pRoot = self.find(parent)
        cRoot = self.find(child)

        if pRoot != cRoot:
            if self.Ar[pRoot] < self.Ar[cRoot]:
                self.Ar[cRoot] = self.Ar[pRoot]
            elif self.Ar[cRoot] > self.Ar[pRoot]:
                self.Ar[pRoot] = self.Ar[cRoot]
            else:
                self.Ar[cRoot] = self.Ar[pRoot]
        print("\tCur Ar:",self.Ar)       

    def paths(self,start,end):
        e_parent = self.find(end)
        s_parent = self.find(start)
        print("\nParent of {} is {}".format(end,start))
        if e_parent == s_parent:
            return True
        else:
            return False
        

    def connections(self,edges):
        e_len = len(edges)
        for i in range(e_len):
            self.union(edges[i][0],edges[i][1])
        pass

        


n = 3
edges = [[0,1],[1,2],[2,0]]
start = 0
end = 2

G = graph(n)
print("Edges        :",edges)
G.connections(edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,G.paths(start,end)))
print("*******************************************************************")
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
start = 2
end = 1

G = graph(n)
print("Edges        :",edges)
G.connections(edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,G.paths(start,end)))
print("*******************************************************************")
n = 1
edges = []
start = 0
end = 0

G = graph(n)
print("Edges        :",edges)
G.connections(edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,G.paths(start,end)))
