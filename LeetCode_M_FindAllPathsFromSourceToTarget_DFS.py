#DFS
def findAllPaths(graph):
    glen = len(graph)
    result = []
    dfs(graph,0,[0],result)
    print("Result:",result)
    

def dfs(graph,curnode,path,result):
    print("\ncurnode:{},path:{},result:{}".format(curnode,path,result))

    if curnode == len(graph)-1:        
        result.append(path)
        print("\n\tpath:{},result:{}".format(path,result))
        
    for n in graph[curnode]:
        dfs(graph,n,path+[n],result)
        curnode = 0
        
    
                
            
   
                
        
        

    
        

    

    



graph = [[1,2],[3],[3],[]]
findAllPaths(graph)
print("***********************************")
graph = [[4,3,1],[3,2,4],[3],[4],[]]
findAllPaths(graph)
print("***********************************")
graph = [[1],[]]
findAllPaths(graph)
print("***********************************")
graph = [[1,2,3],[2],[3],[]]
findAllPaths(graph)
print("***********************************")
graph = [[1,3],[2],[3],[]]
findAllPaths(graph)
print("***********************************")

