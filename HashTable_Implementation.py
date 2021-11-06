#HashTable and HashMaps are the same data structures
#Dictionary is Python specific implementation of HashTable

#similar to __init__, python provides standard operators to set and get functionalities
#eg., __setitem__ can be called using H['key'] = val
#eg., __getitem__ can be called to get the value of a particular key 

#Handle collission with Separate Chaining or Linear Probing

class HashTable():
    def __init__(self):
        self.MAX = 10
        #self.arr = [None for i in range(self.MAX)]
        self.arr = [[] for i in range(self.MAX)] #For Linear Probbing
        #print(self.arr)

    def gethash(self,day):
        sm = 0
        for d in day:
            sm += ord(d)
        return sm%10

##    def add(self,key,val):
    def __setitem__(self,key,val): 
        hsh = self.gethash(key)
        found = False
        for idx,element in enumerate(self.arr[hsh]):
            if len(element) == 2 and element[0] == key:
                self.arr[hsh][idx] = (key,val)
                found = True
                break
        if not found:
                self.arr[hsh].append((key,val))
##            print("\tlen(element):",len(element))
##            print("\t\tElement[0]:",element[0])
##            print("\t\tcheck:",element[0] == key)
##            print(idx,element)
        
        print("\n\tCur HashTable:",self.arr)

##    def get(self,key):
    def __getitem__(self,key):
        hsh = self.gethash(key)
        for element in self.arr[hsh]:
            if element[0] == key:
                print(element[1])

    def __delitem__(self,key):
        hsh = self.gethash(key)
        for index, element in enumerate(self.arr[hsh]):
            if element[0] == key:
                print(self.arr[hsh][index])# = None
                del self.arr[hsh][index]
        print("\n\tHashTable after delete:",self.arr)
        


H = HashTable()
##H.add('march 6',130)
##H.get('march 6')
H['march 6'] = 310
print("\nvalue @H['march 6'] = ",H['march 6'])
H['march 7']= 340
H['march 8']= 380
H['dec 17'] = 27
H['march 17']= 320
H['march 6'] = 300
del H['dec 17']
#print([x for x in H.arr if x is not None])
print("**********************************")
print("Chaining:")
print("\tgethash('march 6'):{}\n\tgethash('march 17'):{}".format(H.gethash('march 6'), H.gethash('march 17')))
#collision is when multiple keys get the same index, this can avoided using Separate Chaining by storing values as linked list
#having linked list will allow multiple values to be stored in the same key
#con is that the time and space complexity will grow

#Linear probbing
#if key is already taken then the array is probed to  find the next possible position to store the data.

H['march 6']
H['march 17']
del H['march 17']
        
    
