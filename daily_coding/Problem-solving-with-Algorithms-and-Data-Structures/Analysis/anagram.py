#Anagram detection

# O(n^2)
def anagrammysolution(s1,s2):
    temps1 = list(s1)
    temps2 = list(s2)

    temps1.sort()
    temps2.sort()

    finals1 ="".join(temps1)
    finals2 = "".join(temps2)

    if finals1 == finals2:
        return True
    return False


#print(anagrammysolution("heart","earth"))

#sacrifices space for speed therefore O(n)
def anagramSolution4(s1,s2):
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK

#print(anagramSolution4('apple','pleap'))


