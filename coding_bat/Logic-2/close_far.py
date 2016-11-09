#Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close(a,b,c):
    value1 = abs(a-b)
    value2 = abs(a-c)
    if value1 <= 1 or value2 <= 1:
        return True
    return False

def far(a,b,c):
    valueAB = abs(a-b)
    valueAC = abs(a-c)
    valueBA = abs(b-a)
    valueBC = abs(b-c)
    valueCA = abs(c-a)
    valueCB = abs(c-b)

    if (valueAB >= 2 and valueAC >= 2) or (valueBA >=2 and valueBC >=2) or (valueCA >=2 and valueCB >=2):
        return True
    return False
    

def close_far(a,b,c):
    if close(a,b,c) == True and far(a,b,c) == True:
        return True
    return False



print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))
print(close_far(4,5,3))
print(close_far(4,3,5))
print(close_far(-1,10,0))
print(close_far(0,-1,10))
print(close_far(10,10,8))
print(close_far(10,8,9))
print(close_far(8,9,10))
print(close_far(8,9,7))
print(close_far(8,6,9))

        
