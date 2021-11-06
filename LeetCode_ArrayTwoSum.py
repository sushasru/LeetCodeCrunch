#Arrays - TwoSum

def twoSum(nums, target):
    indices = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                indices.append(i)
                indices.append(j)
                print("\t\tIndices:{}".format(indices))
                #print("nums[{}]:{},nums[{}]:{}".format(i,nums[i],j,nums[j]))

                      
nums = [2,7,11,15]
target = 9
print("List:{};Target:{}".format(nums,target))
twoSum(nums,target)

nums = [3,2,4]
target = 6
print("List:{};Target:{}".format(nums,target))
twoSum(nums,target)
