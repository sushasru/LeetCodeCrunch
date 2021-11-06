def isHappy(n,sums):
    seen = set()
    notseen = True
    
    while n != 0 and n not in seen:
        print("\nN:",n)
        if sums == 0:
            seen.add(n)
            print("\tSeen:",seen)

        digit = n%10
        sums += digit**2
        n //= 10
        print("\t\tSums:" ,sums)
        print("\t\tn is now:",n)
        if n == 0:
            n = sums
            sums = 0
                
                
            
            
        
        
            
        
    
        
        

            
    print(n)

    print(n==1)
        
    
     
n = 116
isHappy(n,0)
print("\n**********\n")  
n = 19
isHappy(n,0)
print("\n**********\n")
n = 2
isHappy(n,0)
print("\n**********\n")
n = 3
isHappy(n,0)
print("\n**********\n")
n = 7
isHappy(n,0)
