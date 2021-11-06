#Double Linked List Implementation
print("\t\t\tIMPLEMENTATION OF DOUBLE LINKED LIST\n")

class Node():
    def __init__(self,prev=None,data=None,next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoubleLinkedList():
    def __init__(self):
        print("Initializing Double Linked List\n")
        self.head = None

    def insert_at_head(self,data):
        print("\tInsert {} as first node".format(data))
        if self.head is None:
            self.head = Node(None,data,None)
            self.prev = self.head
        else:
            node = Node(None,data,self.head)
            node.prev = self.head
            self.head = node
            print("\t\t\tPrevious Node:",node.prev.data)

    def insert_at_end(self,data):
        print("\tInsert {} as the last node".format(data))
        if self.head is None:
            self.head = Node(None,data,None)
        else:
            itr = self.head
            while itr.next is not None:
                print("\tCurrent node:",itr.data)
                itr = itr.next    
            node = Node(None,data,None)
            node.prev = itr
            itr.next = node
            print("\t\t\tPrevious Node:",node.prev.data)

    def print_reverse_list(self):
        print("\tPrint reverse list\n")
        if self.head is None:
            print("\tEmpty Linked List")
        else:
            itr = self.head
            itr_prev = None

            while itr:
                print("\tCurrent Node:",itr.data)
                print("\tPrevious Node:",itr.prev.data)
                print("\tNext Node:",itr.next.data)
                
                itr.prev = itr.next
                print("\t\tNew Previous Node:",itr.prev.data)
                if itr.prev.next is not None:
                    itr.next = itr.prev.next
                    itr = itr.next
                else:
                    itr.next = itr.prev
                    break

            print("\t\t\tPrevious Node:",itr.prev.prev.data)
            self.head = itr.prev
            self.print()

    def print(self):
        if self.head is None:
            print("\tEmpty Linked List")
        else:
            itr = self.head
            lls = ''
            while itr:
                lls += str(itr.data) + "-->"
                itr = itr.next
            if itr is None:
                print("\nHead-->"+lls+"End\n")
        


d = DoubleLinkedList()
d.insert_at_head(6)
d.print()
d.insert_at_head(16)
d.print()
d.insert_at_head(26)
d.print()
d.insert_at_head(36)
d.print()
d.insert_at_end(46)
d.print()
d.insert_at_end(47)
d.print()
d.print_reverse_list()
