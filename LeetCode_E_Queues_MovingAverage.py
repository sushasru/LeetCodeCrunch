#Moving Average from DataStream
class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = -1
        self.curSize = 0
        self.queue = [None]*size

    def enqueue(self,val):
        print("\nEnqueue {} to queue".format(val))
        print("\t1.Capacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.size,self.curSize,self.head,self.tail))
        if (self.tail+1)%self.size == self.head:
            self.dequeue()

        if self.head >= 0:
            print("\t2.Capacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.size,self.curSize,self.head,self.tail))
            self.tail = (self.tail+1)%self.size
            self.queue[self.tail] = val
            self.curSize += 1
            print("\t3.Capacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.size,self.curSize,self.head,self.tail))

        else:
            self.head = 0
            self.queue[self.head] = val
            self.tail = 0
            self.curSize += 1

    def dequeue(self):
        print("\nDequeue first element from queue")
        print("\tD1.Capacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.size,self.curSize,self.head,self.tail))
        if self.curSize == 0:
            print("\tEmpty Queue")
        elif self.head == self.tail:
            self.head = -1
            self.tail = -1
            self.curSize = 0
        else:
            self.head = (self.head+1)%self.size
            self.curSize -= 1
        print("\tD2.Capacity of the queue:{}, size of the queue:{},head is at:{}, tail is at :{}".format(self.size,self.curSize,self.head,self.tail))
            

    def qprint(self):
        cq = '|'
        if self.curSize == 0:
            print("\tEmpty Queue")
        else:
            if self.tail >= self.head:
                for i in range(self.head,self.tail+1):
                    cq += str(self.queue[i]) + '|'
            else:
                for i in range(self.head,self.tail+1):
                    cq += str(self.queue[i]) + '|'
                for i in range(0,self.size):
                    cq += str(self.queue[i]) + '|'
            print("\n\tQueue:{}\n".format(cq))
            

    def next(self,val):
        self.enqueue(val)
        self.qprint()
        if self.curSize == 0:
            return 0
        else:
            avg = 0
            sum = 0
            if self.tail >= self.head:
                for i in range(self.head,self.tail+1):
                    sum += self.queue[i]
            else:
                for i in range(self.head,self.tail+1):
                    sum += self.queue[i]
                for i in range(0,self.size):
                    sum += self.queue[i]
                    
            avg = sum/self.curSize
            print("\nRunning Average:",round(avg,5))
            
        
        

mav = MovingAverage(3)
mav.next(3)
mav.next(1)
mav.next(10)
mav.qprint()
mav.next(3)
mav.qprint()
mav.next(5)
mav.qprint()
            
            
