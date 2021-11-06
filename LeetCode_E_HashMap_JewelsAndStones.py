def numJewelsInStones(jewels,stones):
    j_set = set(jewels)
    j_count = 0
    print(j_set)
    for s in stones:
        if s in j_set:
            j_count += 1

    print("j_count:",j_count)
    return j_count
    
jewels = "aA"
stones = "aAAbbbb"
print("Result:",numJewelsInStones(jewels,stones))
print("******************************************")
jewels = "z"
stones = "ZZ"
print("Result:",numJewelsInStones(jewels,stones))
