#bidirectional graph with n vertices -> 0 to n-1 (inclusive)
#input - 2D integer array edges[i] = [ui,vi]; ui and vi are the connected vertices
#every vertex pair is connected by atmost one edge, no vertex has an edge to itself
#Determin if path exists from vertex start to vertex end
#return true if valid path exists
        
def findifpathexists(n,edges,start,end):    
    visited = [False for i in range(n)]
    g = [set() for _ in range(n)]
    print(g)
    for i,e in edges:
        g[i].add(e)
        g[e].add(i)

    print("\n graph:{}".format(g))

    bfs(g,visited,start)

    return visited[end]

def bfs(g,visited,v):
    q = []
    q.append(v)
    visited[v] = True
    path = []
    #path.append(v)
    print("\n path:{}\n queue:{}\n visited:{}\n".format(path,q,visited))
    while q:
        node = q.pop(0)
        neigh = g[node]
        for nxt in neigh:
            if visited[nxt] == False:
                q.append(nxt)
                visited[nxt] = True
                #path.append(nxt)
                print("\n path:{}\n queue:{}\n visited:{}\n".format(path,q,visited))
            

            
            
            

    

        


n = 3
edges = [[0,1],[1,2],[2,0]]
start = 0
end = 2

print("Edges :",edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,findifpathexists(n,edges,start,end)))
print("*******************************************************************\n")

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
start = 0
end = 5


print("Edges :",edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,findifpathexists(n,edges,start,end)))
print("*******************************************************************\n")

n = 1
edges = []
start = 0
end = 0


print("Edges :",edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,findifpathexists(n,edges,start,end)))
