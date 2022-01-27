#Given an array of ints length 3, figure out which is larger between the first and last elements in the array, and set all the other elements to be that value. Return the changed array. 
def max_end3(nums):
  value = []
  if nums[0] > nums[2]:
    while len(value) < 3:
      value.append(nums[0])
    return value
  else:
     while len(value) < 3:
      value.append(nums[2])
     return value
