#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
    count = len(str)
    wordcount = 0
    word = ""
    if len(str) <= 1:
        return str
    else:
        while wordcount < count:
            word = word + str[0:wordcount + 1]
            wordcount += 1
        return word
        

print(string_splosion('Code'))
print()
