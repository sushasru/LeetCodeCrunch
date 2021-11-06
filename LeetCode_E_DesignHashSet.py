#HashSet
class MyHashSet:
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range(self.max)]

    def add(self,key):
        hsh = self.gethash(key)
        self.arr[hsh] = key

    def remove(self,key):
        hsh = self.gethash(key)
        self.arr[hsh] = None

    def contains(self,key):
        hsh = self.gethash(key)
        if self.arr[hsh] is not None:
            print("{} exists!".format(key))
            return True
        else:
            print("{} doesnt exist!".format(key))
            return False

    def gethash(self,key):
        print("hash for {} is {}".format(key,key%100))
        return key%self.max

M = MyHashSet()
M.add(1)#set = [1]
M.add(2)#set = [1, 2]
print("Current Hash Set:",M.arr)
M.contains(1)#return True
M.contains(3)#return False, (not found)
M.add(2)#set = [1, 2]
M.contains(2)#return True
print("Current Hash Set:",M.arr)
M.remove(2)#set = [1]
print("Current Hash Set:",M.arr)
M.contains(2)#return False, (already removed
print("Current Hash Set:",M.arr)
