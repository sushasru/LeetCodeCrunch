import copy
def allPathsSourceTarget(graph):
    print("\nGraph:",graph)
    path = bfs(0,graph)
    print("Output:",path)


def bfs(start,graph):
    q = []
    result = []
    q.append([start])
    target = len(graph)-1
    node = []    
    lst = []
    
    while q:
        print("\nq:{};target:{};node:{}".format(q,target,node))
        node = q.pop(0)
        nlen = len(node)-1
        #print(node[nlen])
        lastnode = node[nlen]
        
        print("\tNode:",node)
        print("\t   LastNode:",lastnode)
        if lastnode != target:
            print("{}!={}".format(lastnode,target))
            neigh = graph[lastnode]
            print("\n\tNeigh:",neigh)
            for n in neigh:
                print("\t\tn:",n)
                lst = []
                print("\t\t node:",node)
                lst = copy.deepcopy(node)
                print("\t\t lst:",lst)
                lst.append(n)
            
                print("\t List:",lst)
                q.append(lst)
                print("\t\t Q here:",q)
        else:
            result.append(node)
            print("result:",result)
        print("----------------------------------")
    return result
            
        
            
        
        
    
        

            


graph = [[1,2],[3],[3],[]]
allPathsSourceTarget(graph)
print("********************************")
graph = [[4,3,1],[3,2,4],[3],[4],[]]
allPathsSourceTarget(graph)
print("********************************")




'''
graph = [[1,2],[3],[3],[]]
n = len(graph) => 4
find all the paths between 0 and n-1 i.e 0 to 3

for i,v in enumerate(graph):
    path = bfs(i,v)

bfs starting with 0
    q = []
    q.append(0)
    prev = []
    paths = []

    while q:
        node = q.pop(0)
        neig = g[node]
        for n in neig:
            q.append(n)
            prev.append(node)
        
        
    
'''
