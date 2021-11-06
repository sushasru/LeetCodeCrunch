#Queue implementation using Linked List
class Node():
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

    def dequeue(self):
        print("\nDequeue")
        if self.tail is None:
            print("\tEmpty Queue")
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
        print("\tRemoved {} from queue".format(data))
            

    def enqueue(self,val):
        print("\nAdd {} to the Queue".format(val))
        itr = Node(val,None)
        if self.size == 0:
            self.head = itr
            self.tail = itr
            self.size += 1
            print("\tself.head.data",self.head.data)
            print("\tself.tail",self.tail)
        else:
            print("\n\tself.head.data.next",self.head.data)
            if self.tail is not None:
                print("\tself.tail.data:",self.tail.data)
            self.tail.next = itr
            self.tail = itr
            self.size += 1

    def printlinkedList(self):
        if self.head is None:
            print("\tEmpty Queue")
        else:
            itr = self.head
            lstr = ""
            while itr:
                lstr += str(itr.data)+"|"
                itr = itr.next
            print("\tQueue:",lstr)

q = LinkedList()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.printlinkedList()
q.dequeue()
q.printlinkedList()


            
                






