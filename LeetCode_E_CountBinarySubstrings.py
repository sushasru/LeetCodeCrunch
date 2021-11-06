'''two pointer technique
substrcounter = to keep track of the substrings

sptr , eptr
    - traverses through each element until last element is reached
    - sptr keeps tab of the start of the substring
    - eptr keeps tab of the end of the substring
Z-counter, 1-counter
    - will be used to keep tab of the 0's and 1's

-eptr is reset and moved to sptr to start the next comparison (use while loop since index of sptr changes)

- O(n) time complexity:
    n is the length of the orginal string
- O(1) space complexity since we are not adding to the array
    
'''

def countBinarySubstrings(s):
    
    substr_Counter = 0
    slen = len(s)
    print("strlen = ",slen)
    if slen <= 1:
        return 0
    else:
        sptr = 0
        eptr = 0
        bin_counter = 0
        zero_count = 0
        one_count = 0
       
        while eptr < slen:
            print(s[eptr])
            if s[eptr] == '0':
                bin_counter -= 1
                zero_count += 1
                #print("bin:",bin_counter)
            else:
                bin_counter += 1
                one_count += 1

            print("zero_count:{},one_count:{}".format(zero_count,one_count))

            if bin_counter == 0:
                substr_Counter += 1
                print("\tSubstring:",s[sptr:eptr])
                sptr += 1
                eptr = sptr
                zero_count = 0
                one_count = 0
                print("\nsptr:{},eptr:{}".format(sptr,eptr))
            else:
                eptr += 1
                if bin_counter == 1 and slen-eptr == 0:
                    sptr += 1
                    eptr = sptr
                print("bin_counter:{},char_left:{}".format(bin_counter,slen-eptr))
        print("Substring Count:",substr_Counter)
                    
                
                    
                

                
        
        
    

##s = '00110011'
##countBinarySubstrings(s)
##print("*********************************************")
##s = '10101'
##countBinarySubstrings(s)
##print("*********************************************")
s = '00110'
countBinarySubstrings(s)
