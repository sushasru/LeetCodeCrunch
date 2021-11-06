#Stack using Queues

class MyStack:

    def __init__(self):
        self.s = []

    def push(self,x):
        self.s.append(x)            
        print("After Push:",self.s)

    def pop(self):
        val = self.s.pop()
        print("Popped:",val)
        return val

    def top(self):
        val = self.s[-1]
        print("Top:",val)

    def empty(self):
        if len(self.s) == 0:
            print("Queue is empty!")
            return True
        else:
            print("Queue is not empty!")
            return False
        
        



obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.empty()
