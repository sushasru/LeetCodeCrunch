'* Directed Acyclic graph of n nodes 0 to n-1*'
'* print all the possible paths from 0 to n-1 *'


def allPaths(graph):
    q = []
    visited = [False for i in range(len(graph))]
    path = []

    
    def dfs(visted,graph,vertex,q):
        print("\tVertex is ",vertex)
        q.append(vertex)
        visted[vertex] = True

        for v in graph[vertex]:
            print("\tv:",v)
            path.append(q.pop())
            print("\t\tPath:",path)
            if not visted[v]:
                return dfs(visited,graph,v,q)
            
            
    dfs(visited,graph,0,q)
    path.append(q.pop())
    print("Path:",path)
    print("\n graph:{}\n visited:{}\n".format(q,visited))

    path = []
    dfs(visited,graph,1,q)
    path.append(q.pop())
    print("Path:",path)
    print("\n graph:{}\n visited:{}\n".format(q,visited))
    



graph = [[1,2],[3],[3],[]]
allPaths(graph)
