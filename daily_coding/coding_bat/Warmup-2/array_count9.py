#Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
    if len(nums) == 0:
        return -1
    else:
        count = 0
        for i in nums:
            if i == 9:
                count = count + 1

        return count

print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))
print(array_count9([]))
