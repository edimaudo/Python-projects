
##Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.


def centered_average(nums):
    if len(nums) < 3:
        return -1
    else:
        nums.sort()
        del nums[0]
        del nums[len(nums)-1]
        numsSum = sum(nums)
        numsCount = len(nums)
        output = int(numsSum/numsCount)
        return output 


print(centered_average([1, 2, 3, 4, 100]))
print(centered_average([1, 1, 5, 5, 10, 8, 7]))
print(centered_average([-10, -4, -2, -4, -2, 0]))
print(centered_average([1,1,99,99]))
print(centered_average([5, 3, 4, 6, 2]))
print(centered_average([5, 3, 4, 0, 100]))
print(centered_average([100, 0, 5, 3, 4]))
print(centered_average([1000, 0, 1, 99]))
print(centered_average([6, 4, 8, 12, 3]))
print(centered_average([4, 4, 4, 4, 5]))
print(centered_average([4, 4, 4, 1, 5]))


