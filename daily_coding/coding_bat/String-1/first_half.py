#Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    word = len(str)
    halfword = (word + 1) // 2
    return str[0:halfword]


print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
