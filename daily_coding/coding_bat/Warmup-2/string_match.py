#Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a,b):
    count = 0
    for i, j in zip(range(len(a)-1),range(len(b)-1)):
        if a[i:i+2] == b[j:j+2]:
            count += 1
    return count
##    count = 0
##    for i in range(len(a)-1):
##        for j in range(len(b)-1):
##            if a[i:i+2] == b[j:j+2]:
##                count += 1
##    return count 
                       
                       


print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))
print(string_match('aabbccdd', 'abbbxxd'))
print(string_match('aaxxaaxx', 'iaxxai'))
print(string_match('iaxxai', 'aaxxaaxx'))

