#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
 
#has22([1, 2, 2]) → True
#has22([1, 2, 1, 2]) → False
#has22([2, 1, 2]) → False


def has22(nums):
    for i in range(len(nums)-1):
        if nums[i:i+2] == [2,2]:
            return True
    return False



print(has22([1, 2, 2]))
print(has22([1, 2, 1, 2]))
print(has22([2, 1, 2]))
print(has22([1, 2, 2, 2]))
print(has22([1, 2, 2, 1]))
print(has22([4, 2, 4, 2, 2, 5]))
print(has22([2,2]))


##    if len(nums) < 3:
##        return -1
##    else:
##        for i in nums:
##            if nums[0] == 2 and nums[1] == 2:
##                return True
##            elif nums[-2]== 2 and nums[-1] == 2:
##                return True
##            elif nums[-1] < len(nums)-1 and nums[i] == 2 and nums[i + 1] == 2:
##                return True
##            else:
##                return False
