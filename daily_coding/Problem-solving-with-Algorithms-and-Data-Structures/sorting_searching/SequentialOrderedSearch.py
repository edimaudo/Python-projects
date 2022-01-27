def orderedSequentialSearch(alist,item):
    for i in alist:
        if i == item:
            return True
        elif i > item:
            return False
        

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))
