#Remove from LinkedList
class Node():
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_to_list(self,val):
        if self.head is None:
            self.head = Node(val,None)
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = Node(val,None)

    def convertListToLinkedList(self,lst):
        for i in lst:
            if self.head is None:
                temp = Node(i,None)
                self.head = temp
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = Node(i,None)

    def list_print(self):
        if self.head is None:
            print("\tEmpty Linked List")
        else:
            itr = self.head
            lstr = ""
            while itr:
                lstr += str(id(itr.val))+":"+str(itr.val)+ "-->"
                itr = itr.next

            print("Head-->"+lstr+"End")

    def RemoveElements(self,el):
        if self.head is None:
            print("Empty Linked List")
            return self.head
        else:
            prev = Node(None,None)
            cur = self.head
            print("Self.head:{}@{}".format(self.head.val,id(self.head.next)))

            while cur:
                print("\tPrev:{},Cur:{}".format(prev.val,cur.val))
                if cur.val == el:
                    print("\t\tCur val is ",cur.val)
                    if prev.val is not None:
                        print("\t\t\tPrev is not None.it is ",prev.val)
                        #print("\t\t\tPrev:{},Cur.next:{}".format(prev.val,cur.next))
                        prev.next = cur.next
                        cur = cur.next
                    else:
                        
                        cur = cur.next
                        self.head = cur
                        #print("\t\t\tPrev is None.Update head pointer ",)
                else:
                    print("\t\tCur val is {}, Move On!".format(cur.val))
                    prev = cur
                    cur = cur.next
        return self.head

    def isPalindrome(self):
        if self.head is None:
            print("Empty Linked List")
            return False
        else:
            dictn = {}
            itr = self.head
            while itr:
                if itr.val in dictn:
                    dictn[itr.val] += 1
                else:
                    dictn[itr.val] = 1
                itr = itr.next

            print("\tDictionary:",dictn)

    def ReverseList(self):
        if self.head is None:
            return False
        else:
            prev = Node(None,None)
            itr = self.head
            while itr.next:
                print("\tAt Node:",itr.val)
                if prev.val is None:
                    prev = itr.next
                    print("\t\tPrev is now {}@{}".format(prev.val,id(prev.val)))
                    itr.next = None
                else:
                    tmp = itr.next
                    itr.next = prev
                    prev = tmp
                    print("\t\t\tPrev is now {}@{}".format(prev.val,id(prev.next)))

                print("\t\tprev.next:",prev.next)  
                if prev.next:
                    itr = prev
                    print("\t\t\titr is now {}@{}".format(itr.val,id(itr.next)))
                else:
                    print("Here")
                    self.head = itr

            self.head = itr

                
            
           
                
                
                    
                    
                
                
                


def RemoveFromList(lst,num):
    for i in lst:
        if i == num:
            lst.remove(i)
    print("\tResulting List:",lst)

L2 = LinkedList()
lst = [1,2,6,3,4,5,6]
L2.convertListToLinkedList(lst)
L2.list_print()
L2.ReverseList()
L2.list_print()
print("*****************************************\n")

##L2 = LinkedList()
##lst = [1,2,2,1]
##L2.convertListToLinkedList(lst)
##L2.list_print()
##L2.isPalindrome()
##print("*****************************************\n")

##lst = [1,2,6,3,4,5,6]
##print("Current List:",lst)
##RemoveFromList(lst,6)
##print("*****************************************\n")
##L1 = LinkedList()
##L1.insert_to_list(3)
##L1.insert_to_list(4)
##L1.list_print()
##print("*****************************************\n")
##L2 = LinkedList()
##lst = [1,2,6,3,4,5,6]
##L2.convertListToLinkedList(lst)
##L2.list_print()
##L2.RemoveElements(6)
##L2.list_print()
##print("*****************************************\n")
##L3 = LinkedList()
##lst = [1,2,1]
##L3.convertListToLinkedList(lst)
##L3.list_print()
##L3.RemoveElements(1)
##L3.list_print()
##print("*****************************************\n")
##L3 = LinkedList()
##lst = [1,2,1]
##L3.convertListToLinkedList(lst)
##L3.list_print()
##L3.RemoveElements(2)
##L3.list_print()
##print("*****************************************\n") 
##L2 = LinkedList()
##lst = []
##L2.convertListToLinkedList(lst)
##L2.list_print()
##L2.RemoveElements(1)
##L2.list_print()
##print("*****************************************\n")
##L2 = LinkedList()
##lst = [7,7,7,7]
##L2.convertListToLinkedList(lst)
##L2.list_print()
##L2.RemoveElements(7)
##L2.list_print()
##print("*****************************************\n")
##L3 = LinkedList()
##lst = [7]
##L3.convertListToLinkedList(lst)
##L3.list_print()
##L3.RemoveElements(7)
##L3.list_print()
##print("*****************************************\n")
##L3 = LinkedList()
##lst = [1,2]
##L3.convertListToLinkedList(lst)
##L3.list_print()
##L3.RemoveElements(1)
##L3.list_print()
    

