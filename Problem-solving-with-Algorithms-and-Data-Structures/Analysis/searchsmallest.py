#find smallest value in random list in n log n time & n time
#timeit.timeit(function here,number=10000)
#n log n time

import timeit
def findsmallest(listval):
    listval.sort()
    return str(listval[0])

#n time
def findsmallest2(listval):
    smallest = listval[0]
    for i in listval:
        if smallest > i:
            smallest = i
    return str(smallest)


def main():
    listval = [100,8,3,7,14,5,4,69,72,1,36]
    t1 = timeit.timeit(findsmallest(listval),number=10000)
    t2 = timeit.timeit(findsmallest2(listval),number=10000)
    print (t1)
    print (t2)



main()

