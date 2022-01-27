import timeit
import timer
import random


def testlistindex(listdata,indexvalue):
    try:
        tempvalue = listdata.index(indexvalue)
        return str(tempvalue)
    except:
        return "-1"

def listtest():
    list1 = [1,2,3,4,5,6]
    list2 = [1,2,3,4,5,6,7,8,9,10,12,13,14,16,18,19,23,100,340,321,453,542,1234]
    list3 = [2,4,1,6,8,7]
    list4 = [12,9,6,5,3,2,33,43,46,78,65,31,45,78,901,62,145,88,93,86,51,99,12]
    list5 = list1
    list6 = list2
    list7 = list3
    list8 = list4

    list1random = random.randint(0,len(list1)-1)
    list2random = random.randint(0,len(list2)-1)
    list3random = random.randint(0,len(list3)-1)
    list4random = random.randint(0,len(list4)-1)

    list1time = timeit.timeit(testlistindex(list1,list1[list1random]),number=10000)
    list2time = timeit.timeit(testlistindex(list2,list2[list2random]),number=10000)
    list3time = timeit.timeit(testlistindex(list3,list3[list3random]),number=10000)
    list4time = timeit.timeit(testlistindex(list4,list4[list4random]),number=10000)
    list5time = timeit.timeit(testlistindex(list5,7),number=10000)
    list6time = timeit.timeit(testlistindex(list6,200),number=10000)
    list7time = timeit.timeit(testlistindex(list7,20),number=10000)
    list8time = timeit.timeit(testlistindex(list8,100),number=10000)

    print (list1time)
    print (list2time)
    print (list3time)
    print (list4time)
    print (list5time)
    print (list6time)
    print (list7time)
    print (list8time)

listtest()

