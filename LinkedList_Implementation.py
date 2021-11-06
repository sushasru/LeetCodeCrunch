#Singly Linked List Implementation
class Node():
    def __init__(self,data=None,next=None):
        #print("\n***Initialized Node***\n")
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        print("\n***Initialized Head***\n")
        self.head = None

    def insert_as_firstNode(self,data):
        print("\tCreating first Node")
        node = Node(data,self.head)
        self.head = node

    def insert_as_lastNode(self,data):
        print("\tInsert as Last Node")
        if self.head is None:
            self.insert_as_firstNode(data)
        else:
            itr = self.head
            while itr.next:
                #print("\t\tNow at node:",itr.data)
                itr = itr.next
                
            itr.next = Node(data,None)

    def insert_at_index(self,data,index):
        print("\tInsert {} at Position {}".format(data,index))
        if self.head is None:
            if index > 0:
                print("\tEmpty Linked List, We can only insert at position 0")
                return
            elif index == 0:
                self.insert_as_firstNode(data)
            else:
                print("\tIndex should be a positive integer")
                return
        else:
            counter = 0
            itr = self.head
            while counter < index-1:
                #print("\t\tData at index - {} is {}".format(counter,itr.data))
                itr = itr.next
                counter += 1
            #print("\t\tCounter is now:",counter)
            #print("\t\titr.data:{}, itr.next:{}, itr.next.next.data:{}".format(itr.data,itr.next.data,itr.next.next.data))
            node = Node(data,itr.next)
            itr.next = node

    def delete_first_node(self):
        print("\n\tDelete First Node")
        if self.head is None:
            print("\tCannot delete from an empty linked list!!")
        else:
            node = self.head.next
            self.head = node

    def delete_last_node(self):
        print("\n\tDelete Last Node")
        if self.head is None:
            print("\tCannot delete from an empty linked list!!")
        else:
            itr = self.head
            while itr.next.next is not None:
                #print("\t\tAt node:",itr.data)
                itr = itr.next
            #print("\n\t\tAt node:",itr.data)
            itr.next = None

    def delete_node_atIndex(self,index):
        print("\tDelete node from index-{}".format(index))
        if self.head is None:
            print("\nCannot delete from an Empty Linked List")
        else:
            if index < self.lengthofLinkedList():
                counter = 0
                itr = self.head
                while counter < index-1:
                    print("\t\tAt node:",itr.data)
                    itr = itr.next
                    counter += 1
                print("\t\tCurrent Node:",itr.data)
                if itr.next is not None:
                    itr.next = itr.next.next
                else:
                    return
            else:
                print("\tCannot delete since index > length of linked list")
                return
            
    def getvalue_of_firstNode(self):
        print("\tGet value of first node")
        if self.head is None:
            print("\tEmpty Linked List!")
            return
        else:
            print("\t\t\tValue of first node:",self.head.data)
            return self.head.data

    def getvalue_of_lastNode(self):
        print("\tGet value of last node")
        if self.head is None:
            print("\tEmpty Linked List!")
            return
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next
            print("\t\t\tLast Node Value:",itr.data)
        return itr.data
        
    def getvalue_of_NodeatIndex(self,index):
        print("\tGet vaue of node at index - {}".format(index))
        if self.head is None:
            print("\tEmpty Linked List")
            return
        else:
            if index < self.lengthofLinkedList():
                counter = 0
                itr = self.head
                while counter < index:
                    itr = itr.next
                    counter += 1
                print("At index - {} node value is {}".format(index,itr.data))
                return itr.data
            else:
                print("\tIndex greater than length of linked list")
                return
        
    def lengthofLinkedList(self):
        length = 0
        itr = self.head
        while itr:
            length += 1
            itr = itr.next
        print("Linked List Length:{}\n".format(length))
        return length

    def print_reverse_list(self):
        #sample linked list will be Head->Node1->Node2->Node3->Node4->End
        #To reverse a list we can set Node1.next = Null and Node2.next = Node1 and so on until end and finally set Head as Node4
        #I think we need a temporary variable to store the next value for the next iteration
            #Example, temp = Node1.next.next i.e., store Node2.next value in Temp
            #         Node1.next.next = Node1
            #         Node1.next = None
            #         head => Node1.next.next, temp.Next 
            itr = self.head
            while itr:
                if itr.next.next is not None:
                    print("\tCurrent Node:",itr.data)
                    temp = itr.next
                    itr.next.next = itr
                    itr.next = None
                else:
                    head = itr
                    
    def convertListtoLinkedList(self,lst):
        for i in lst:
            print("\tAdding {} to LinkedList:".format(i))
            if self.head is None:
                self.head = Node(i,None)
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                print("\t\tAdd node after :",itr.data)
                itr.next = Node(i,None)

    def removeElements(self,lst,val):
        if self.head is None:
            print("Cannot remove elements from Empty Linked List")
        else:
            tortoise = self.head
            hare = self.head.next
            print("\tTortoise is at {} and Hare is at {}".format(tortoise.data,hare.data))
            counter = 0
            while tortoise and hare:
                print("index {} & {}".format(counter,counter+1))
                if hare:
                    print("\t\tTortoise is at {} and Hare is at {}".format(tortoise.data,hare.data))
                    
                    if tortoise.data == val:
                        while tortoise.data== val and tortoise.next and hare.next:
                            tortoise = tortoise.next
                            self.head = tortoise
                            hare = hare.next
                            #print("\t\t\tTortoise is now at {} and Hare is now at {}".format(tortoise.data,hare.data))
                        if tortoise.next is None or hare.next is None:
                            self.head = None
                            return None
                    if hare.data == val:
                        print("\t\t\tMove tortoise from {} to Hare's position {}".format(tortoise.data,hare.data))
                        if hare.next is not None:
                            tortoise.next = hare.next
                            hare = hare.next
                        else:
                            tortoise.next = None
                            break
                    
                        
                else:
                    tortoise.next = None
                    
                tortoise = tortoise.next
                hare = hare.next
                counter += 1
                    
                    
                
                
                
                
                
                    
        
    def print(self):
        if self.head is None:
            print("\nEmpty Linked List\n")
            return
        else:
            itr = self.head
            llstr = ''
            while itr:
                llstr += str(itr.data) + "-->"
                #print(llstr)
                itr = itr.next
                
            if itr is None:
                print("\nHead-->"+llstr+"End\n")
           
        


ll = LinkedList()
lst = [1,2,6,3,4,5,6]
ll.convertListtoLinkedList(lst)
ll.print()
ll.removeElements(lst,6)
ll.print()
print("*************************\n")
l2 = LinkedList()
lst = []
l2.convertListtoLinkedList(lst)
l2.print()
l2.removeElements(lst,1)
l2.print()
print("*************************\n")
l3 = LinkedList()
lst = [7,7,7,7]
l3.convertListtoLinkedList(lst)
l3.print()
l3.removeElements(lst,7)
l3.print()
print("*************************\n")
l4 = LinkedList()
lst = [1]
l4.convertListtoLinkedList(lst)
l4.print()
l4.removeElements(lst,1)
l4.print()
print("*************************\n")
##ll.insert_at_index(14,3)
##ll.print()
##ll.insert_at_index(14,0)
##ll.print()
##ll.insert_as_firstNode(2)
##ll.insert_as_firstNode(10)
##ll.insert_as_lastNode(1)
##ll.print()
##ll.insert_as_lastNode(15)
##ll.insert_as_lastNode(25)
##ll.insert_as_lastNode(6)
##ll.insert_as_lastNode(100)
##ll.print()
##ll.lengthofLinkedList()
##ll.insert_at_index(4,2)
##ll.print()
##ll.delete_first_node()
##ll.print()
##ll.delete_last_node()
##ll.delete_last_node()
##ll.delete_last_node()
##ll.print()
##ll.delete_node_atIndex(2)
##ll.print()
##ll.delete_node_atIndex(2)
##ll.print()
##ll.delete_node_atIndex(2)
##ll.print()
##ll.delete_node_atIndex(2)
##ll.print()
##ll.getvalue_of_firstNode()
##ll.getvalue_of_lastNode()
##ll.getvalue_of_NodeatIndex(4)
##ll.insert_as_firstNode(2)
##ll.insert_as_lastNode(20)
##ll.insert_as_lastNode(1110)
##ll.insert_at_index(0,-1)
##ll.print()
##ll.getvalue_of_NodeatIndex(4)
###ll.print_reverse_list()

