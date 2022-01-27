#Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
    if len(str) >= 3:
        return 3*(str[0]+str[1]+str[2])
    else:
        return 3*str
