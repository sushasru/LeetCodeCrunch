#Stack implementation
import sys
class Stack():
    def __init__(self):
        self.stack = []
        self.front = -1
        self.tail = -1
        self.size = 0
        

    def push(self,val):
        print("\nPUSH\n")
        if self.size == 0:
            self.front = 0
            self.tail = 0
            self.stack.append(val)
            self.size += 1
            
        else:
            self.tail += 1
            self.stack.append(val)
            self.size += 1
            

    def pop(self):
        print("\nPOP\n")
        print("self.head:{},self.tail:{}".format(self.front,self.tail))
        if self.size == 0:
            print("self.head:{},self.tail:{},Empty Stack".format(self.front,self.tail))
        else:
            self.stack.pop()
            self.tail -= 1
            self.size -= 1
            print("self.head:{},self.tail:{}".format(self.front,self.tail))
            if self.tail == -1:
                self.front = -1

    def top(self):
        if self.size == 0:
            print("Empty Stack")
        else:
            print("\nTop:{}\n".format(self.stack[self.tail]))
            return self.stack[self.tail]

    def getMin(self):
        if self.size == 0:
            print("Empty Stack!")
        else:
            minval = sys.maxsize #2147483647
            #print("\n\tdefault minval:",minval)
            for i in range(self.tail,self.front-1,-1):
                minval = min(minval,self.stack[i])
            print("\nMin Value:",minval)
            return minval

    def sprint(self):
        if self.size == 0:
            print("self.head:{},self.tail:{},Empty Stack".format(self.front,self.tail))
        else:
            for i in range(self.tail,self.front-1,-1):
                #print(i)
                print("\t{}\n\t__".format(self.stack[i]))

ms = Stack()
ms.push(2147483646)
ms.push(2147483646)
ms.push(2147483647)
ms.sprint()
ms.top()
ms.pop()
ms.sprint()
ms.getMin()
ms.pop()
ms.sprint()
ms.getMin()
ms.pop()
ms.sprint()
ms.push(2147483647)
ms.sprint()
ms.top()
ms.getMin()
ms.push(-2147483648)
ms.sprint()
ms.top()
ms.getMin()
ms.pop()
ms.sprint()
ms.getMin()
ms.sprint()


    
