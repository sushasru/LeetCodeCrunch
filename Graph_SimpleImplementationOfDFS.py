#DFS
def DepthFirstSearch(graph):
    print("\nGraph:",graph)
    lg = len(graph)    
    visited = [False for i in range(lg)]
    path = []

##This piece of code is only required if graph is represented as list of edges
##eg., [(0,1),(0,2),(1,3),(2,3)]
##    g = [[] for i in range(lg)]
##    for v in graph:
##        if len(v)>1:
##            g[v[0]].append(v[1])
##    print("g:",g)
    
    st = []
    print("DFS:",dfs(0,visited,g,st))

def dfs(curnode,visited,graph,st):
    print("\tcurnode:{}\n\tvisited:{}".format(curnode,visited))
    st.append(curnode)
    visited[curnode] = True

    neigh = graph[curnode]
    print("\t\t\tneigh:{}".format(neigh))
    for ni in neigh:
        if visited[ni] == False:
            dfs(ni,visited,graph,st)
    return st

                
        
        

    
        

    

    



graph = [[1,2],[3],[3],[]]
DepthFirstSearch(graph)
print("***********************************")
graph = [[4,3,1],[3,2,4],[3],[4],[]]
DepthFirstSearch(graph)
print("***********************************")
graph = [[1],[]]
DepthFirstSearch(graph)
print("***********************************")
graph = [[1,2,3],[2],[3],[]]
DepthFirstSearch(graph)
print("***********************************")
graph = [[1,3],[2],[3],[]]
DepthFirstSearch(graph)
print("***********************************")
graph = [[1,9],[0,8],[3],[2,4,5,7],[],[6],[7],[3,6,8,10,11],[7],[8],[11],[7,10],[12]]
DepthFirstSearch(graph)
