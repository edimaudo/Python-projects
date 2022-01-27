#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
  if n + 10 >= 100 and n - 10 <=100:
    return True
  elif n + 10 >= 200 and n - 10 <=200:
    return True
  else:
    return False
