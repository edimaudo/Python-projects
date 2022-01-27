# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.

def near_ten(num):
    value = num
    value2 = num % 10
    if value2 == 8 or value2 == 9 or value2==1 or value2==2 or value2 == 0:
        return True
    return False


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))
print(near_ten(10))
