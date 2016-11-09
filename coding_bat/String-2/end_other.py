#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    if b.endswith(a) or a.endswith(b):
        return True
    return False

print(end_other('hiabc','abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
    
