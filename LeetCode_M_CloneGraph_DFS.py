#[[2,4],[1,3],[2,4],[1,3]]
#   1     2     3     4

#Initialize the nodes first without the neighbors
#Add neighbors through depth first search

import collections
class Node:
    def __init__(self,val=0,neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        print("\t\tInitialized Node with val:{} and neighbors:{}".format(self.val,self.neighbors))


class Solution:
    def cloneGraph(self,node: 'Node'):
        print("Node:",node)
        if not node:
            return node            
        seen = {}     #key->index:value->node itself
        deque = collections.deque(node)
        print(deque)
       
        while deque:
            print("\nBEFORE\n seen:{}\n deque:{}".format(seen,deque))
            nd = deque.popleft()
            print("\tnd:",nd)
            if nd not in seen:
                seen[nd] = Node(nd.val)
            neigh = node[nd-1]
            print("\t Neigh:",neigh)
            for n in neigh:
                if n not in seen:
                    seen[n] = Node(n)
                    deque.append(n)
                seen[nd].neighbors.append(seen[n])
            print("\nAFTER\n seen:{}\n deque:{}".format(seen,deque))
        print(seen[node])
        return seen[node]
        

        

        
        
                    


        



adjList = [[2,4],[1,3],[2,4],[1,3]]
s = Solution()
s.cloneGraph(adjList)
