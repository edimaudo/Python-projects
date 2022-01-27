# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

def make_chocolate(small, big, goal):
    realBig = big*5
    if big == 0:
        return -1
    elif realBig == goal:
        return T
    else:
        remainder = 0
        if goal > realBig:
            remainder = goal - realBig
        else:
            remainder = goal % 5
        return small >= remainder
    



print(make_chocolate(4, 1, 9))
print(make_chocolate(4, 1, 10))
print(make_chocolate(4, 1, 7))


