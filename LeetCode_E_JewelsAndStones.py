#numJewelsInStones
def numJewelsInStones(jewels,stones):
    j_set = {}
    jewelinstones = 0 
    for i in range(len(jewels)):
        if jewels[i] in j_set:
            j_set[jewels[i]] += 1
        else:
            j_set[jewels[i]] = 1

    for j in range(len(stones)):
        print(stones[j])
        if stones[j] in j_set:
            jewelinstones += 1
            print(jewelinstones)

    return jewelinstones
            


jewels = "aA"
stones = "aAAbbbb" #3
print("Jewels : {}, Stones: {}".format(jewels,stones))
print("{} jewels are in {}".format(numJewelsInStones(jewels,stones),stones))
print("*************************************")
jewels = "z"
stones = "ZZ" #3
print("Jewels : {}, Stones: {}".format(jewels,stones))
print("{} jewels are in {}".format(numJewelsInStones(jewels,stones),stones))
print("*************************************")
