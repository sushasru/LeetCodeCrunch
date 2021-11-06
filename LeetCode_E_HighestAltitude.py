import sys
#Highest Altitude
def hAltitude(gain):
    high = -sys.maxsize - 1
    temp = 0 
    for i in range(0,len(gain)):
        temp += gain[i]
        print("Cur temp:",temp)
        if temp > high:
            high = temp        
        #print("Temp new:",temp)
    print("high:",high)

gain = [-5,1,5,0,-7]
print("Gains:",gain)
hAltitude(gain)
