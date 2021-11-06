class Node():
    def __init__(self,val = None, next = None):
        self.val = val
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None


    def convertListToLinkedList(self,lst):
        for l in lst:
            print("\tAdd l:{}".format(l))
            if self.head is None:
                n = Node(l,None)
                self.head = n
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = Node(l,None)

    def printLinkedList(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            itr = self.head
            lstr = ""
            while itr:
                lstr += str(itr.val)+"-->"
                itr = itr.next

            print("Head-->"+lstr+"End")

    def reverseLinkedList(self):
        prv = Node(None,None)
        nxt = self.head
        itr = self.head
        if self.head is None:
            return self.head
        else:
            while itr.next:
                print("\tprv:{},nxt:{}".format(prv.val,nxt.val))
                nxt = itr.next
                if prv.val is not None:
                    itr.next = prv
                else:
                    itr.next = None
                prv = itr
                itr = nxt
                print("\t\tprv:{},nxt:{}".format(prv.val,nxt.val))
            
            if prv.val is not None:
                itr.next = prv

            self.head = itr

    def rotateRight(self,k):
        if self.head is None:
            print("\tEmpty LinkedList")
        else:
            i = 0
            length = 0
            itr = self.head
    
            while itr:
                nd = itr
                itr = itr.next
                length += 1

            print("\t\t\tLength of LinkedList:",length)
            if k > 500:
                k = k%length
                print("\t\t\tk:",k)
                 
            while i < k:
                print("\tRotate {}:".format(i))
                itr = self.head
                nd = Node(None,None)
                while itr.next:
                    print("\t\titr.val:",itr.val)
                    nd = itr
                    itr = itr.next
                    length += 1
                
                print("\t\t\tPrevious to last element:",nd.val)
                print("\t\t\tlastelement:",itr.val)

                nd.next = None
                itr.next = self.head
                self.head = itr
                i += 1
                self.printLinkedList()
            
    






L1 = LinkedList()
lst = [5,4,3,2,1]#[2,1]#[3,2,1]#[1]#[2,1,0]#[5,4,3,2,1]#[]#[1,-2,-5,0,-4]#[1,2,3,4,5]#
L1.convertListToLinkedList(lst)
L1.printLinkedList()
L1.reverseLinkedList()
L1.printLinkedList()
#L1.rotateRight(2)
#L1.printLinkedList()
L1.rotateRight(10)
