#implement queu using stack
class MyQueue:
    def __init__(self):
        self.st = []
        
    def push(self,x):
        print("Push ",x)
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            return False
        else:
            return self.st.pop(0)

    def peek(self):
        if len(self.st) == 0:
            return False
        else:
            print("Peek:",self.st[0])
            return self.st[0]

    def empty(self):
        if len(self.st) == 0:
            return True
        else:
            return False

mq = MyQueue()
mq.push(1)
mq.push(2)
mq.push(3)
mq.push(4)
print(mq.pop())
mq.push(5)
print(mq.pop())
print(mq.pop())
print(mq.pop())
print(mq.pop())

        

    
