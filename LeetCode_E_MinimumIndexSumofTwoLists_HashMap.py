def findRestaurant(list1,list2):
    dictn = {}
    for idx,item in enumerate(list1):
        if item in list2 and item not in dictn:
            dictn[item] = idx + list2.index(item)
    print(dictn)
    return [k for k,v in dictn.items() if v == min(dictn.values())]

   
            

        
##    for key,values in dictn.items():
##        print("key:{},value:{}".format(key,values))
##        if key in list2:
##            print("\tindex of {} in list2 is {}".format(key,list2.index(key)))
##            dictn[key] += list2.index(key)
##        else:
##            del dictn[key]
       


##    print(dictn)

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print("\n Found {} from list1: {} and list2: {}\n".format(findRestaurant(list1,list2),list1,list2))
print("********************************************************************************\n")
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print("\n Found {} from list1: {} and list2: {}\n".format(findRestaurant(list1,list2),list1,list2))
print("********************************************************************************\n")
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
print("\n Found {} from list1: {} and list2: {}\n".format(findRestaurant(list1,list2),list1,list2))
print("********************************************************************************\n")
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
print("\n Found {} from list1: {} and list2: {}\n".format(findRestaurant(list1,list2),list1,list2))
print("********************************************************************************\n")
list1 = ["KFC"]
list2 = ["KFC"]
print("\n Found {} from list1: {} and list2: {}\n".format(findRestaurant(list1,list2),list1,list2))
print("********************************************************************************\n")
list1 = ["Shogun"]
list2 = ["KNN"]
print("\n Found {} from list1: {} and list2: {}\n".format(findRestaurant(list1,list2),list1,list2))
