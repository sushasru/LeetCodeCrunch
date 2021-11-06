cache = {}
def fact(n):
    #print("N is {}".format(n))
    if n in cache:
        return cache[n]
    
    if n <= 0:
        print("\tone")
        result = 1
    elif n == 1:
        print("\t1")
        result = 1
    else:
        result = n*fact(n-1)
    cache[n] = result
    return result

cache = {}
def fib(n):
    #print("\nn:{}\n".format(n))
    if n in cache:
        print("\t{} is in cache - {}".format(n,cache))
        return cache[n]
    
    if n <= 0:
        print("\tn = ",n)
        result = 0
    elif n == 1 :
        print("\tn is one")
        result = 1
    else:
        result = fib(n-1) + fib(n-2)

    print("\tresult:",result)
    cache[n] = result
    return result


def powr(x,n):
    def pwrhelper(x,n):
        print("\tx:{},n:{}".format(x,n))
        
        if n == 0:
            return 1
        elif n == 1:
            return x
        R = pwrhelper(x,n//2)
        print(R)
        if int(n%2) == 0:
            return R*R
        else:
            return R*R*x
        
    
    if n < 0 :
        print ("here")
        n *= -1
        print("n:{}".format(n))
        return 1/pwrhelper(x,n)
    else:
        return pwrhelper(x,n)

        

    
    

n = -2
x = 2.00000 #0.25
#print("{} factorial = {}".format(n,fact(n)))
#print("*****************************************")
#print("Fib({}) = {}".format(n,fib(n)))
print("*****************************************")
print("{}^{} = {}".format(x,n,powr(x,n)))
n = 0.00001
x = 2147483647
print("*****************************************")
print("{}^{} = {}".format(x,n,powr(x,n)))
