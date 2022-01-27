#Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}. 
def rotate_left3(nums):
    temp = nums[0]
    nums[0] = nums[1]
    nums[1] = nums[2]
  
    nums.remove(nums[2])
    nums.append(temp)
    return nums
