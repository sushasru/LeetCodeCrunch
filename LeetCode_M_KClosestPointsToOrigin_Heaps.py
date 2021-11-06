import math
def kClosest(points,k):
    print("\nGet {} points closest to origin from {}\n".format(k,points))

    for i,pt in enumerate(points):
        #print("\npt:",pt)
        dist = EucDist(pt[0],pt[1])
        points[i].append(dist)

    print("\nPoints with Distance:",points)

    l = len(points)-1

    print("\nLength:",l)

    for i in range(int(l/2),0,-1):
        MaxHeap(points,i,l)

    print("\nHeap:",points)
    
    for i in range(l,0,-1):               
        points[i], points[0] = points[0], points[i]
        print("\nUpdated Heap:",points) 
        MaxHeap(points,0,i)
        

    

    result = []
    print("MaxHeap:",points)
    for i in range(k):
        result.append([points[i][0],points[i][1]])

    return result
        
    

    


def MaxHeap(points,curidx,l):
    
    largest = curidx

    lidx = 2*curidx + 1
    ridx = 2*curidx + 2

    if lidx > l:
        lidx = None

    if ridx > 1:
        ridx = None

    print("\n\tCurIDX:{};lidx:{},ridx:{}".format(curidx,lidx,ridx))
    if lidx is not None and points[largest][2] < points[lidx][2]:
        print("\t1){}vs{}".format(points[largest][2],points[lidx][2]))
        largest = lidx

    if ridx is not None and points[largest][2] < points[ridx][2]:
        print("\t{}vs{}".format(points[largest][2],points[ridx][2]))
        largest = ridx

    if largest != curidx:
        points[curidx], points[largest] = points[largest], points[curidx]
        MaxHeap(points,largest,l)

    return points
    
        
    

def EucDist(x,y):
    return round(math.sqrt((0-x)**2+(0-y)**2),3)
    

##points = [[1,3],[-2,2]]
##k = 1
##print("Result:",kClosest(points,k))
##print("*****************************************")
##points = [[3,3],[5,-1],[-2,4]]
##k = 2
##print("Result:",kClosest(points,k))
##print("*****************************************")
points = [[-2,10],[-4,-8],[10,7],[-4,-7]]
k = 3
print("Result:",kClosest(points,k))
print("*****************************************")
