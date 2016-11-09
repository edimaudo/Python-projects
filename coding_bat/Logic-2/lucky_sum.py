#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

def lucky_sum(a,b,c):
    if a != 13 and b != 13 and c!= 13:
        return a + b + c
    elif a == 13 and b != 13 and c != 13:
        return 0
    elif a != 13 and b == 13 and c != 13:
        return a
    elif a != 13 and b != 13 and c == 13:
        return a + b
    elif a == 13 and b == 13 and c != 13:
        return 0
    elif a == 13 and b != 13 and c == 13:
        return 0
    elif a != 13 and b == 13 and c == 13:
        return a


print(lucky_sum(1, 2, 3))
print(lucky_sum(1, 2, 13))
print(lucky_sum(1, 13, 3))
print(lucky_sum(1, 13, 13))
print(lucky_sum(6, 5, 2))
print(lucky_sum(13, 2, 13))
print(lucky_sum(3, 3, 13))
print(lucky_sum(13, 13, 2))

