#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
    wordValue = []
    for i in range(len(str)):
        if i % 2 == 0:
            wordValue.append(str[i])
    return''.join(wordValue)
    

print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))
