#Datastructures
print("\t\t1.LISTS\n")
#1.Lists
l = [1,2,3,1,2,0,90]
l.sort()
print("sorted list:",l)
print("\n--------------------------------------------------------------\n")
print("\t\t2.TUPLES\n")
#2.Tuples
##declare
colors = ('black','blue','white')
print("colors: ",colors)
##add item
colors = colors+('yellow',)
print("appended tuple:",colors)
##Access an item in tuple
print("access item colors[0]:",colors[0])
##Update an existing tuple
colors2 = ('Purple','Pink','Brown')
colors3 = colors + colors2
colors3
print("--------------------------------------------------------------\n")
#3.Dictionaries
print("\t\t3.DICTIONARIES\n")
myDict = {'name':'Susha','occupation':'sw','country':'USA'}
print("Dictionary",myDict)
print("Access Name: Dictionary['name'] -",myDict['name'])
print("Access Country: Dictionary.get('country') -",myDict['country'])
myDict['country'] = "America"
print("Dictionary updated :",myDict)
myDict['state'] = 'Virginia'
print("Dictionary updated :",myDict)
myDict.pop('country')
print("Dictionary updated :",myDict)
print("--------------------------------------------------------------\n")
#4.Sets
print("\t\t4.SETS\n")
mySet = {2,3,1,4}
print("My Set:",mySet)
print("Sent Length:",len(mySet))
print("2 in mySet:",2 in mySet)
print("5 in mySet:",5 in mySet)
##Union of sets
set2 = {6,7,8,3}
union_set = mySet | set2
print("Union set:",union_set)
##Intersection of sets
intersection_set = mySet & set2
print("Common values:",intersection_set)
##Set difference
setdiff = mySet - set2
print("Elements in mySet but not in set2:",setdiff)
setdiff = set2 - mySet
print("Elements in set2 but not in mySet:",setdiff)
mySet.remove(4)
print(mySet)
mySet.remove(0)
print(mySet)
