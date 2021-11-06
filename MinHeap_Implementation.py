class MinHeap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.heap = [0]*self.capacity
        self.size = 0
        print("Initialized heap - {} with capacity {}; current size is {}".format(self.heap,self.capacity,self.size))

    def getParentIndex(self,cur_idx):
        return -(cur_idx//-2)-1

    def getLchildIndex(self,cur_idx):
        return (2*cur_idx)+1

    def getRchildIndex(self,cur_idx):
        return (2*cur_idx)+2

    def getMinVal(self):
        return self.heap[0]

    def hasParent(self,cur_idx):
        return self.getParentIndex(cur_idx) >= 0

    def hasLchild(self,cur_idx):
        return self.getLchildIndex(cur_idx) < self.size

    def hasRchild(self,cur_idx):
        return self.getRchildIndex(cur_idx) < self.size

    def parent(self,cur_idx):
        return self.heap[self.getParentIndex(cur_idx)]

    def lchild(self,cur_idx):
        return self.heap[self.getLchildIndex(cur_idx)]

    def rchild(self,cur_idx):
        return self.heap[self.getRchildIndex(cur_idx)]

    def isFull(self):
        #print("size:{},capacity:{}".format(self.size,self.capacity))
        return self.size == self.capacity

    def swap(self,idx1,idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def insert(self,lst):
        for n in lst:
            #print(self.isFull())
            if self.isFull():
                print("\tHeap is Full")
            else:
                self.heap[self.size] = n
                self.size += 1
                #self.heapifyUp()#iterative
                self.heapifyUp(self.size-1) #recursive
                self.printHeap()

    def removeMin(self):
        if self.size == 0:
            print("\tHeap is Null")
        else:
            print("Removing {} from {}".format(self.heap[0],self.heap))
            #data = self.heap[0]
            self.heap[0] = self.heap[self.size-1]
            self.size -= 1
            #self.heapifyDown()#iterativ
            self.heapifyDown(0)#recursive
            self.printHeap()
            
            

    def heapifyUp(self): #iterative
        print("Iterativ")
        cur_idx = self.size-1
        while(self.hasParent(cur_idx) and self.parent(cur_idx) > self.heap[cur_idx]):
            self.swap(self.getParentIndex(cur_idx),cur_idx)
            cur_idx = self.getParentIndex(cur_idx)

    def heapifyUp(self,cur_idx):
        if(self.hasParent(cur_idx) and self.parent(cur_idx) > self.heap[cur_idx]):
            self.swap(self.getParentIndex(cur_idx),cur_idx)
            self.heapifyUp(self.getParentIndex(cur_idx))

    def heapifyDown(self):#iterative
        cur_idx = 0
        while self.hasLchild(cur_idx):
            self.printHeap()
            minChildIdx = self.getLchildIndex(cur_idx)
            if self.hasRchild(cur_idx) and self.rchild(cur_idx) < self.lchild(cur_idx):
                minChildIdx = self.getRchildIndex(cur_idx)
            if self.heap[cur_idx] < self.heap[minChildIdx]:
                break
            else:                
                self.swap(cur_idx,minChildIdx)
            
            cur_idx = minChildIdx

    def heapifyDown(self,cur_idx): #log(n) -> T.C and S.C
        self.printHeap()
        minChildIdx = cur_idx
        if self.hasLchild(cur_idx) and self.heap[cur_idx] > self.lchild(cur_idx):
            minChildIdx = self.getLchildIndex(cur_idx)
        if self.hasRchild(cur_idx) and self.heap[minChildIdx] > self.rchild(cur_idx):
            minChildIdx = self.getRchildIndex(cur_idx)
        if minChildIdx != cur_idx:
            self.swap(cur_idx,minChildIdx)
            self.heapifyDown(minChildIdx)
                          


    def printHeap(self):
        if self.size != 0:
            print("\tHeap: ",self.heap[:self.size])
        else:
            print("Empty Heap")
        
        
                
        



Mh = MinHeap(9)
Mh.insert([14,28,5,6,2,8,10,7,11])
Mh.removeMin()
Mh.removeMin()
Mh.removeMin()
Mh1 = MinHeap(7)
Mh1.insert([0,5,10,20,8,15,30])
Mh1.removeMin()
Mh1.removeMin()
Mh1.removeMin()
Mh2 = MinHeap(4)
Mh2.insert([5,2,3,1])
