#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
 
#sum67([1, 2, 2]) → 5
#sum67([1, 2, 2, 6, 99, 99, 7]) → 5
#sum67([1, 1, 6, 7, 2]) → 4
def sum67(value):
    value2 = [item for item in range(len(value)) if value[item] == 6]
    value3 = [item for item in range(len(value)) if value[item] == 7]
    if value2 = []:
        return sum(value)
    elif value = []:
        return 0
    elif len(value2)<2:
        if value2[0] > value3[0]:
            maxValue2 = max(value2)
            maxValue3 = max(value3)
            value[maxValue2:maxValue3 + 1] = [0] * (maxValue3+1 - maxValue2)
            return sum(value)
        else:
            minValue2 = min(value2)
            minValue3 = min(value3)
            value[minValue2:minValue3 + 1] = [0] * (minValue3+1 - minValue2)
            return sum(value)
    elif
            


        
print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]) )
print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]))
print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]))
print(sum67([2, 7, 6, 2, 6, 7, 2, 7]))
print(sum67([2, 7, 6, 2, 6, 2, 7]))
print(sum67([1, 6, 7, 7]))
print(sum67([6, 7, 1, 6, 7, 7]))
print(sum67([6, 8, 1, 6, 7]))
print(sum67([]))
print(sum67([6, 7, 11]))
print(sum67([11, 6, 7, 11]))
print(sum67([2, 2, 6, 7, 7]))



