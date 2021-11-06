#First Bad Version
#specification - state the problem
    # 1. We want to find the  bad version from a given an array of versions.
    # 2. Use the API to get the first bad version
    # 3. All versions after the first bad version will be bad

#documentation - say what the program will do
    # 1. Binary Search - dividing 
    # 2. min =1, max = n, index = n/2
    # 3. while(min<max):
    # 4.    isBadVersion(index)?
    # 5.        yes -> max = index, index = (max+min)/2
    # 6.        no -> n[index:n]
#implementation - 
#optimization - 

n =5
bad = 4
