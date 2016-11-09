#Given an array of ints, return True if .. 1, 2, 3, .. appears in the array somewhere.

def array123(nums):
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    if nums[0:3] == [1,2,3]:
        return True
    return False
        

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))

