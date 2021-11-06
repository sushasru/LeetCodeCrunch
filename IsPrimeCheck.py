i = 2
n = 80
count = 0
while i*i <= n:
    print("i: ",i)
    if n%i == 0:
        print(n," is not a prime number")
        count = 0
        break
    else:
        count += 1
    i+=1

if count != 0:
    print(n," is a prime number")
    
    
