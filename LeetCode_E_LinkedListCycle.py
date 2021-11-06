#LinkedListCycle
class Node():
    def __init__ (self,val = None, next = None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__ (self):
        self.head = None

    def converttoLinkedList(self,lst):
        for l in lst:
            if self.head is None:
                nd = Node(l,None)
                self.head = nd
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = Node(l,None)
                
    def hasCycle(self):
        dictn = {}
        if self.head is None:
            print("\tNo Cycle")
            return False
        else:
            t = self.head
            if self.head.next.next is not None:
                h = self.head.next.next
                print("h.val:",h.val)

                while h:
                    print("\tTurtle@{} and hare@{}".format(t.val,h.val))
                    if h.val not in dictn:
                        dictn[h.val] = 1
                    if t.val in dictn:
                        print("\tCycle!")
                        return True
                    h = h.next
                    t = t.next
                print("\tNo Cycle!")
                return False

                

            
            

    def printLinkedList(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            itr = self.head
            lstr = ""
            while itr:
                lstr += str(itr.val)+"@"+str(id(itr.val))+"-->"
                itr = itr.next
            print("Head-->"+lstr+"End")


L1 = LinkedList()
lst = [3,2,0,4,2]
L1.converttoLinkedList(lst)
L1.printLinkedList()
print("Is cyclic? {}".format(L1.hasCycle()))

                
    
