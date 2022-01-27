def sequentialSearch(alist,item):
    for i in alist:
        if i == item:
            return True
        return False

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
