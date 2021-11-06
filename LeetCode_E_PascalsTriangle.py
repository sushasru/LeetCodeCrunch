def pascalstriangle(rows):
    tri = []
    temp = []
    for i in range(0,rows):
        print("\n")
        print(len(tri))
        for j in range(0,i+1):
            print("i:{},j:{}".format(i,j))
            if i == 0:
                print("{}\t".format('1'),end="")
                temp.append(1)
            elif j == 0 or j == i:
                print("{}\t".format('1'),end="")
                temp.append(1)
            else:
                print("here")
                print("{}\t".format(j),end="")
                print("tri[{}][{}]:{}+tri[][{}]:{}".format(i-1,j-1,tri[i-1][j-1],i-1,j,tri[i-1][j]))
                temp.append(tri[i-1][j-1]+tri[i-1][j])
        tri.append(temp)
        print("\nTri:",tri)
        temp = []

def recPascalTriable(tri,rows,r,c):
    print("\nrows:{},r:{},c:{},tri:{}\n".format(rows,r,c,tri))
    if r == c or c == 1:
        tri.append(1)
        print("\t2)Tri:",tri)
        return 1
    print("3)rows:{},r:{},c:{},tri:{}".format(rows,r,c,tri))
    return recPascalTriable(tri[r-1][c-1],rows,r,c) + recPascalTriable(tri[r-1][c],rows,r,c)
    
    
        
            

        
  
        
            


#pascalstriangle(5)
tri = [[]*5]*5
print(tri)
#pascalstriangle(5)
print("**********************")
print(recPascalTriable(tri,3,4,3))
