#Return True if the string "cat" and "dog" appear the same number of times in the given string.

def cat_dog(str):
    word1 = 'cat'
    word2 = 'dog'
    word1count = 0
    word2count = 0
    for i in range(len(str)-2):
        if str[i] + str[i+1] + str[i+2] == word1:
            word1count+=1
        elif str[i] + str[i+1] + str[i+2] == word2:
            word2count+=1
    return word1count==word2count


print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
