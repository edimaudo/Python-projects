#count_evens
#Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
 
#count_evens([2, 1, 2, 3, 4]) → 3
#count_evens([2, 2, 0]) → 3
#count_evens([1, 3, 5]) → 0

def count_evens(nums):
    if len(nums) == 0:
        return 0
    else:
        sum = 0
        for i in nums:
            if i % 2 == 0:
                sum += 1
        return sum

print (count_evens([2, 1, 2, 3, 4]))
print (count_evens([2, 2, 0]))
print (count_evens([1, 3, 5]))
print (count_evens([]))
print (count_evens([1]))
print (count_evens([2]))


