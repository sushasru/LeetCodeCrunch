#class without chaining
##*********************************
##class MyHashMap:
##    def __init__(self):
##        self.size = 10
##        self.arr = [None for i in range(self.size)]
##        #print(self.arr)
##
##    def put(self,key,val):
##        hsh = self.gethash(key)
##        self.arr[hsh] = val
##
##    def get(self,key):
##        print("Get value at {}:{}".format(key,self.arr[self.gethash(key)]))
##        return self.arr[self.gethash(key)]
##
##    def remove(self,key):
##        self.arr[self.gethash(key)] = None
##
##    def gethash(self,key):
##        #print("\thash of {} is {}".format(key,key%self.size))
##        return key%self.size


#class with chainging
class MyHashMap:
    def __init__(self):
        self.size = 100
        self.arr = [[] for i in range(self.size)]

    def gethash(self,key):
        print("hash of {} is {}".format(key,key%self.size))
        return key%self.size

    def put(self,key,val):
        print("\nPUT ",val)
        hsh = self.gethash(key)
        found = False
        for i,v in enumerate(self.arr[hsh]):
            print("i:{},v:{}".format(i,v))
            if v:
                if v[0] == key:
                    print(v)
                    arr[hsh][i] = (key,val)
                    found = True
                    break
        if found == False:
            self.arr[hsh].append((key,val))
            print("\tCurrent Arr:",self.arr)

    def get(self,key):
        print("\nGET ",key)
        hsh = self.gethash(key)
        for v in self.arr[hsh]:
            if v[0] == hsh:
                print("value of {} is {}".format(v[0],v[1]))
                return v[1]
        return -1

    def remove(self,key):
        hsh = self.gethash(key)
        for i,v in enumerate(self.arr):
            if v[0] == key:
                print("{} to be deleted".format(self.arr[hsh][i]))
                self.arr[hsh][i] = None
                
        

M = MyHashMap()
M.put(1,1)
M.put(2,2)
M.put(11,3)
M.get(1)
M.get(3)
print(M.arr)
