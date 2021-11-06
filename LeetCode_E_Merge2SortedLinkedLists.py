class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def createLinkedList(self,lst):    
        for i in lst:
            if self.head is None:
                self.head = Node(i,None)            
            else:
                nd = self.head
                while nd.next:
                    nd = nd.next
                nd.next = Node(i,None)

    def createList(self,val):
        if self.head is None:
            self.head = Node(val,None)
        else:
            nd = self.head
            while nd.next:
                nd = nd.next
            nd.next = Node(val,None)
                    

    def printLinkedList(self):
        print("printing")
        if self.head is None:
            return None
        else:            
            n = self.head
            lstr = ""
            while n:                
                lstr+= str(n.data)+"->"
                n = n.next

            print("Head->{}End".format(lstr))
            return "Head->{}End".format(lstr)
            
            
            

#correct the code for the test case l1:[1], l2[]
def MergeLists(llist1,llist2):
    Link3 = LinkedList()

    def MergeHelper(llist1,llist2,Link3):
        if not llist1 or not llist2:
            if llist1:
                Link3.createList(llist1.data)
            if llist2:
                Link3.createList(llist2.data)
            return Link3
        
        print("l1:{},l2:{}".format(llist1.data,llist2.data))
        if llist1.data < llist2.data:
            print(llist1.data)
            Link3.createList(llist1.data)
            return MergeHelper(llist1.next,llist2,Link3)
        if llist2.data < llist1.data:
            print(llist2.data)
            Link3.createList(llist2.data)
            return MergeHelper(llist1,llist2.next,Link3)
        if llist1.data == llist1.data:
            print(llist1.data)
            print(llist2.data)
            Link3.createList(llist1.data)
            Link3.createList(llist2.data)
            return MergeHelper(llist1.next,llist2.next,Link3)            
       

    MergeHelper(llist1,llist2,Link3)
    print(Link3.printLinkedList())
    return Link3
        
    
#another test case: L1:[1,2,4], L2:[1,3,4]           
    

l1 = [1]
l2 = []
Link1 = LinkedList()
Link1.createLinkedList(l1)
print("\nLinkedList1: {}\n".format(Link1.printLinkedList()))

Link2 = LinkedList()
Link2.createLinkedList(l2)
print("\nLinkedList2: {}\n".format(Link2.printLinkedList()))

print("Merge L1:{} and L2:{} to form -> {}".format(l1,l2,print(MergeLists(Link1.head,Link2.head))))

