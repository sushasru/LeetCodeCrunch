#2D Array and Matrix implementation


T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
T.insert(2, [0,5,11,13,6])
T[1] = [0,1,0,1,0]
print(T)
T[1][0] = -1
print(T)
del T[1]
print(T)
for r in T:
    for c in r:
        print(c,end=" ")
    print()
print("-------------------------------------------------------------")

##a = [['Mon',18,20,22,17],['Tue',11,18,21,18],
##		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
##		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
##		   ['Sun',13,15,19,16]]
##m = reshape(a,(7,5))
##print(m)
        
l = [1,2,3]
t = (1,2,3)
print(type(l))
print(type(t))

print("-------------------------------------------------------------")

import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res = collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# Print all the elements from the result
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()


x = [[foo for i in range(10)] for j in range(10)]
print(x)
