#bidirectional graph with n vertices -> 0 to n-1 (inclusive)
#input - 2D integer array edges[i] = [ui,vi]; ui and vi are the connected vertices
#every vertex pair is connected by atmost one edge, no vertex has an edge to itself
#Determin if path exists from vertex start to vertex end
#return true if valid path exists
#NOTT WORKING#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,lst):
        n = self.head
        for i in lst:
            if n is None:
                n = Node(i)
                self.head = n
            else:
                n.next = Node(i)
            
        self.printlst()
    
        
    def printlst(self):
        if self.head is None:
            return
        else:
            n = self.head
            lst = ""
            while n:
                lst += str(n.data)+"->"
                n = n.next
            print("Head->{}End".format(lst))
                
        
def findifpathexists(n,edges,start,end):
    adj_list = [[] for i in range(n)]
    visited = [0 for i in range(n)]
    

    for i,v in enumerate(edges):
        print("\ni:{},v:{} => ".format(i,v),end="")
        adj_list[i] = LinkedList()
        adj_list[i].insert(v)

    print("\nAdj_List:{}\nVisited :{}\n".format(adj_list,visited))

    def dfs(node):
        node.printlst()
        st = []
        n = node.head
        while n:
            print("\tNode is at:",n.data)            
            st.append(n.data)
            visited[n.data] = 1
            
            while st:                
                print("\t",st.pop())
                n = n.next
                if n:
                    if visited[n.data] != 1:
                        st.append(n.data)
                        visited[n.data] = 1
                        print("\t\tst:{},visited:{}".format(st,visited))
                    
            n = n.next
                    
            

    print("\n\t****DFS****\n")
    print(type(adj_list[0]))
    for i,node in enumerate(adj_list):
        print("\nList -",i,end="; ")
        dfs(node)

    

        


n = 3
edges = [[0,1],[1,2],[2,0]]
start = 0
end = 2

print("Edges :",edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,findifpathexists(n,edges,start,end)))
print("*******************************************************************\n")

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
start = 2
end = 1


print("Edges :",edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,findifpathexists(n,edges,start,end)))
print("*******************************************************************\n")

n = 1
edges = []
start = 0
end = 0


print("Edges :",edges)
print("\nIs there a path between {} and {}?: {}".format(start,end,findifpathexists(n,edges,start,end)))
