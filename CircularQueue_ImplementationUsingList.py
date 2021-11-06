#Circular queue implementation using List
class Cir_queue():
    
    def __init__(self,capacity):
        print("\nQUEUE INITIALIZATION")
        self.cirQ = [None] * capacity
        self.head = -1
        self.tail = -1
        self.size = 0
        self.capacity = capacity

    def isFull(self):
        #print("\n\tSIZE OF QUEUE:",self.size)
        #print("\tQUEUE CAPACITY:",self.capacity)
        return self.size == self.capacity

    def enqueue(self,val):
        print("\nAdding {} to the queue".format(val))
            
        if (self.tail + 1)%self.capacity == self.head:
            print("Queue is full")
            return False
        elif self.head >= 0:
            #print("\tCapacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.capacity,self.size,self.head,self.tail))
            #self.tail = 0
            #print("\tcurrent tail index:",self.tail)
            self.tail = (self.tail + 1)%self.capacity
            self.cirQ[self.tail] = val
            #self.tail += 1
            self.size += 1
            print("\t1.Capacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.capacity,self.size,self.head,self.tail))
            return True
        else:
            print("\tAdding {} to an empty queue".format(val))
            self.tail = 0
            self.head = 0
            self.cirQ[self.tail] = val
            self.size += 1
            #self.tail += 1
            print("\t2.Capacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.capacity,self.size,self.head,self.tail))
            return True
            
                

    def dequeue(self):
        print("\nRemove first element from the queue")
        print("\tCapacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.capacity,self.size,self.head,self.tail))
        
        if self.size == 0:
            print("Empty Queue")
        elif self.head == self.tail:
            self.head = -1
            self.tail = -1
            self.size = 0
            return True
        else:
            #data = self.cirQ[self.head]
            self.head = (self.head + 1)%self.capacity
            self.size -= 1
            print("\tCapacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.capacity,self.size,self.head,self.tail))
            return True

    def Front(self):
        print("HERE")
        if self.isEmpty() == True:
            print("HEREHERE")
            return -1
        else:
            print("Front:",self.cirQ[self.head])
            return self.cirQ[self.head]

    def Rear(self):
        if self.isEmpty() == True:
            return 0
        else:
            print("\tCapacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.capacity,self.size,self.head,self.tail))
            print("Rear:",self.cirQ[self.tail])
            return self.cirQ[self.tail]


    def isEmpty(self):
        if self.size == 0:
            print("\tEmpty Queue")
            return True
        else:
            print("\tQueue is not Empty! Size =",self.size)
            return False
            
                
            
    def printQueue(self):
        if self.size == 0:
            print("\tEmpty Queue")
        else:
            cque = " | "
            #print("\tCapacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.capacity,self.size,self.head,self.tail))
                        
            if self.tail >= self.head:
                for i in range(self.head, self.tail+1):
                    cque += str(self.cirQ[i])+" | "
            else:
                for i in range(self.head,self.tail+1):
                    cque += str(self.cirQ[i])+" | "
                for i in range(0,self.capacity):
                    cque += str(self.cirQ[i])+" | "

            print("\nQUEUE:{}\n".format(cque))
            
        
                
cq = Cir_queue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.printQueue()
cq.dequeue()
cq.printQueue()
cq.enqueue(3)
cq.printQueue()
print("*******************************************************\n")


cq = Cir_queue(3)
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.printQueue()
cq.Rear()
cq.printQueue()
cq.isFull()
cq.dequeue()
cq.printQueue()
cq.enqueue(4)
cq.printQueue()
cq.Rear()
cq.printQueue()
print("*******************************************************\n")
cq = Cir_queue(8)
cq.enqueue(3)
cq.enqueue(9)
cq.enqueue(5)
cq.enqueue(0)
cq.printQueue()
cq.dequeue()
cq.printQueue()
cq.dequeue()
cq.printQueue()
cq.isEmpty()
cq.isEmpty()
cq.printQueue()
cq.Rear()
cq.printQueue()
cq.Rear()
cq.printQueue()
cq.dequeue()
cq.printQueue()




##cq.dequeue()
##
##cq.isEmpty()
##cq.isEmpty()
##cq.printQueue()
##
##
##cq.dequeue()
##cq.printQueue()

