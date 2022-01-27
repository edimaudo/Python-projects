#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(nums):
    if nums == []:
        return 0
    elif 13 not in nums:
        return sum(nums)
    else:
        if nums[len(nums)-1] == 13:
            nums[len(nums)-1] = 0
            for item, index in enumerate(nums):
                if index == 13:
                    nums[item] = 0
                    nums[item + 1] = 0
            return sum(nums)
        else:
            for item, index in enumerate(nums):            
                if index == 13:
                    nums[item] = 0
                    nums[item + 1] = 0
            return sum(nums)
                
            
        

print (sum13([1, 2, 2, 1])) #6
print (sum13([1, 1]))#2
print (sum13([1, 2, 2, 1, 13]))#6
print (sum13([]))#0
print (sum13([1, 2, 13, 1, 2,13]))#5
print (sum13([13, 2, 1, 1, 2]))#4
print(sum13([13, 1, 2, 13, 2, 1, 13]))#3
print(sum13([13, 0]))#0
print(sum13([13, 1, 13]))#0
print(sum13([1, 2, 13, 2, 1, 13]))
