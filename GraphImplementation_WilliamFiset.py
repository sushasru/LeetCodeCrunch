'''
Ultimate Graph Implementation
    1. Use an un directed graph with edge list
               1  12 - 2   4
             /  \ |     \ /
            10    8      3
             \   /     /
               9     7 - 6 - 5
                \  /  |
                  0 - 11
                   
    2. Convert to adjacency list
    3. Implement dfs
    4. check if 2 points are connected using dfs
    5. Implement bfs
    6. Construct path between a to b
    7. Root the graph
    8. Find center of the graph
    9. Root the graph again - check if thers any difference between 7 and 8
    9. Add a new graph, check if 2 graphs are isomorphic
    10. Create a weighted DAG
    11. Implement Topological sorting
    12. Find Shorted Path
    13. Find the Longest Path
'''

def AdjList(ge, n):
    adlist = [[] for i in range(n)]
    print(adlist)

    for v in ge:
        adlist[v[0]].append(v[1])

    print("Adjacency List:",adlist)
    return adlist

def DFS(adlist, n):
    visited = [None for i in range(n)]
    q = [0]
    path = []    

    while q:
        #print("Visited:{}\nQ:{}\nCurrent Path:{}".format(visited,q,path))
        node = q.pop()
        #print("\tCurrent visiting node ",node)
        visited[node] = True
        neigh = adlist[node]
        #print("\t\tNeighbors of {} -> {}".format(node,neigh))
        for n in neigh:
            if visited[n] == None:
                q.append(n)

        if node not in path:
            path.append(node)
    print("DFS Path:",path)

    
    















#g1 - Edge List
#n1 - No. of Nodes
n1 = 13
g1 = [(0,9),(0,7),(0,11),
      (1,8),(1,10),
      (2,3),(2,12),
      (3,2),(3,4),(3,7),
      (4,3),
      (5,6),
      (6,5),(6,7),
      (7,0),(7,3),(7,6),(7,11),
      (8,1),(8,9),(8,12),
      (9,0),(9,8),(9,10),
      (10,1),(10,9),
      (11,0),(11,7),
      (12,2),(12,8)]

g1_adlist = AdjList(g1,n1)
DFS(g1_adlist,n1)
