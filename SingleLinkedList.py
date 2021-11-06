#LinkedList - Single 
class Node():
    def __init__(self,d):
        self.data = d
        self.next = None
        print("\tInitialized Node: data = {};next = {}".format(self.data,self.next))


class LinkedList():
    def __init__(self):
        self.Head = None
        print("\tCreated HeadNode:",self.Head)

    def AddNodeAtFirst(self,Node):
        print("\nInsert Node as the first element of Linked List")
        if not(self.Head):
            Node.next = self.Head
            self.Head = Node 
            self.TraverseList()
        else:
            newNode = Node
            newNode.next = self.Head
            self.Head = newNode
            self.TraverseList()

    def AddNodeAtLast(self,Node):
        print("\nInsert Node as the last element of Linked List")
        if not(self.Head):
            self.AddNodeAtFirst(Node)
        else:
            n = self.Head
            while n.next is not None:
                n = n.next
            lastNode = Node
            n.next = lastNode
            lastNode.next = None
            self.TraverseList()
            
    def AddNodeAfterItem(self,i,Node):
        print("\nInsert Node after item - {} in the linked list".format(i))
        if not(self.Head):
            self.AddNodeAtFirst(Node)
        else:
            n = self.Head
            while n.next is not None:
                if n.data == i:
                    newNode = Node
                    newNode.next = n.next
                    n.next = newNode
                    n = n.next
                else:
                    n=n.next
        self.TraverseList()    

    def AddNodeBeforeItem(self,i,Node):
        print("\nInsert Node after item - {} in the linked list".format(i))
        if not(self.Head):
            print("here?")
            self.AddNodeAtFirst(Node)
        else:
            n = self.Head
            while n.next is not None:
                print("here")
                print("d:",n.data)
                #n=n.next
                print("d1:",n.data)
                if n.next.data == i:
                    print("cur node:",n.data)
                    print("next node:",n.next.data)
                    print("reached")
                    newNode = Node
                    newNode.next = n.next
                    n.next = newNode
                    n = n.next
                    break
                else:
                    n = n.next
        self.TraverseList()
                
    def DeleteFirstNode(self):
        print("\nDelete First item from linked list")
        if not (self.Head):
            print("No node to delete")
        else:
            n = self.Head
            self.Head = n.next
        self.TraverseList()

    def DeleteLastNode(self):
        print("\nDelete Last item from linked list")
        if not (self.Head):
            print("No node to delete")
        else:
            n = self.Head
            while n.next is not None:
                if n.next.next is None:
                    n.next = None
                    break
                else:
                    n = n.next
        self.TraverseList()

    def DeleteBeforeItem(self,i):
        print("\nDelete node before item-{} from Linked List".format(i))
        if not self.Head:
            print("No node to delete")
        else:
            n = self.Head
            prev = self.Head
            while n.next is not None:
                print("d:",n.data)
                print("prev:",prev.data)
                #n=n.next
                #print("d1:",n.data)
                if n.data == i:
                    if prev == self.Head:
                        print("h")
                        self.Head = prev.next
                        n = n.next
                        break
                    else:
                        print("p:",prev.data)
                        print("d2:",n.data)
                        prev.next = n.next
                        n = n.next
                        break
                else:
                    prev = n
                    n = n.next
                
                
        self.TraverseList()
            
    def TraverseList(self):
        print("Linked List :",end=" ")
        if self.Head is None:
            print("Linked List is empty")
        else:
            n = self.Head
            while n is not None:
                print("{}->".format(n.data),end=" ")
                n = n.next
            print("None")

L = LinkedList()
L.DeleteFirstNode()
L.AddNodeAtLast(Node(4))
L.AddNodeAtFirst(Node(1))
L.AddNodeAtFirst(Node(2))
L.AddNodeAtLast(Node(3))
L.AddNodeAfterItem(4,Node(8))
L.AddNodeBeforeItem(8,Node(10))
L.AddNodeBeforeItem(4,Node(12))
L.DeleteFirstNode()
L.DeleteLastNode()
L.DeleteBeforeItem(12)
L.DeleteBeforeItem(10)
#L.TraverseList()
