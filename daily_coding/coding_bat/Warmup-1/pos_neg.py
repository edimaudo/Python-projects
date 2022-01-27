#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if ((a < 0 and b > 0) or (a > 0 and b < 0)) and negative == False:
      return True
    elif (a < 0 and b < 0) and negative == True:
      return True
    else:
      return False
