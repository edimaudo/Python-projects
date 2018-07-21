alist = [54, 72, 78, 49, 65, 63, 75, 67, 54]

def getMedian(alist):
    if alist == []:
        return []
    else:
        alist = sorted(alist)
        count = len(alist)
        if count % 2 != 0:
            median = alist[(count - 1)//2]
        else:
            value1 = alist[(count-1)//2]
            value2 = alist[count//2]
            median = (value1+value2)/2
    return median


def getAbsoluteStandardDeviation(alist, median):
    if alist == []:
        return 0
    else:
        sumvalue = 0
        alist = sorted(alist)
        count = len(alist)
        for value in alist:
            sumvalue+= abs(value - median)
        return sumvalue/count

print(getAbsoluteStandardDeviation(alist,getMedian(alist))) 
#print (getMedian(alist))


