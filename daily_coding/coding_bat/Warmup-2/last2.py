#Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
    if len(str) < 2:
        return 0
    else:
        word = ""
        word = word + str[-2] + str[-1]
        count = 0
        for i in range(len(str)-2):
            if str[i:i+2] == word:
                count+=1
        return count


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))

    
