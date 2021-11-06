#implement Queue using Array or List
class queue():
    def __init__(self,capacity):
        print("INITIALIZING QUEUE")
        self.qu = [None]*capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def isFull(self):
        print("\tCHECKING IF QUEUE IS FULL")
        return self.capacity == self.size
            
    def enqueue(self,val):
        print("\nADDING TO THE QUEUE END")
        if self.isFull():
            print("\tQueue Is Full. Cannot add any new elements")
        else:
            self.qu[self.tail] = val
            self.tail += 1
            self.size += 1
            

    def dequeue(self):
        print("\nREMOVING FROM THE QUEUE FRONT")
        if self.size == 0:
            print("\tCannot dequeue from an empty queue")
        else:
            data = self.qu[self.head]
            self.head += 1
            self.size -= 1
            if self.head == self.tail:
                self.head = 0
                self.tail = 0
                self.size = 0
            
        print("\tDequeued {} from queue".format(data))
        

    def printQueue(self):
        if self.size == 0:
            print("\tEmpty Queue")
        else:
            i = self.head
            q_str = ""
            while i<self.tail:
                q_str += str(self.qu[i])+"|"
                i += 1
            print("\nQUEUE:- {}\n".format(q_str))


q = queue(10)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)
q.enqueue(11)
q.printQueue()
q.dequeue()
q.printQueue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.printQueue()
q.dequeue()
q.dequeue()
q.printQueue()


            
        
