# Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
    for i in range(len(str)-1):
        return (str[i] + str[i + 1])*2

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))
