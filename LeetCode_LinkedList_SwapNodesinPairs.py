class Node:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = None
        #print("Node initialized")

class LinkedList:
    def __init__(self):
        self.head = None
        print("initialized Linked List")


    def insertNode(self,data):
        for d in data:
            #print(d)
            if self.head is None:
                self.head = Node()
                self.head.val = d
                self.head.next = None
            else:
                nd = self.head
                newnd = Node(d)
                while nd.next:
                    nd = nd.next
                    #print(nd.val)
                nd.next = newnd
                newnd.next = None

    def printList(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            nd = self.head
            lst = ""
            while nd:
                lst += str(nd.val) + "->"
                nd = nd.next

            print("Head->"+lst+"None")

    def swapPairs(self):
        if self.head is None:
            return None
        else:
            nd = self.head
            self.swap(nd,nd)

    def swap(self,prevnode,curnode):
        if curnode is None:
            print("****End of LinkedList***")
            return
        
        #print("\tPrevNode:{},CurNode:{},NextNode:{}".format(prevnode.val,curnode.val,curnode.next.val))

        temp = curnode.next.next
        curnode.next.next = curnode
        
        if self.head == curnode:
            self.head = curnode.next
        else:
            prevnode.next = curnode.next

        curnode.next = temp
              
        print("\n\tPrevNode:{},CurNode:{},NextNode:{}\n".format(prevnode.val,curnode.val,temp))
        self.printList()
        self.swap(curnode,temp)
        
                

                


l = LinkedList()
lst = [1]
l.insertNode(lst)
l.printList()
l.swapPairs()
l.printList()
