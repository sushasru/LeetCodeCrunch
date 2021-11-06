##Demonstrate Queue library in Python
from collections import deque
from queue import Queue

mq = Queue(maxsize =3)
mq.put(1)
mq.put(2)
mq.put(3)
print(mq.get())
mq.get()

q = deque()


q.append(1)
q.append(2)
q.append(3)

print(q)


print(q.popleft())
print(q)
print(q.popleft())
print(q)
print(q.popleft())
print(q)
if q:
    print("Non empty")
    print(q.popleft())
else:
    print("Empty")
    print(q)




