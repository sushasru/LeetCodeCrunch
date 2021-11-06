def removePalindromeSub(s):
    print("String:",s)
    sptr = 0
    eptr = len(s)-1
    rem_counter = 0
    pal_counter = 0
    while sptr < eptr:
        if s[sptr] == s[eptr]:
            sptr += 1
            eptr -= 1
            pal_counter += 2
        else:
            rem_counter += 1
            eptr -= 1
        print("\tpalcounter:{},remcounter:{}".format(pal_counter,rem_counter))
    if rem_counter == 0:
        print("string is a palindrome, hence output = 1")
        return 1
    else:
        print("No of operations = ",rem_counter)
        return rem_counter
            
            




s = "ababa"
removePalindromeSub(s)
print("*************************************")
s = "abb"
removePalindromeSub(s)
print("*************************************")
s = "baabb"
removePalindromeSub(s)
print("*************************************")
