from math import floor

def factors(n):
 result = []
 for i in range(2,n+1): # test all integers between 2 and n
  s = 0;
  while n/i == floor(n/float(i)): # is n/i an integer?
   n = n/float(i)
   s += 1
  if s > 0:
   for k in range(s):
    result.append(i) # i is a pf s times
   if n == 1:
    return result

# test
print factors(90)