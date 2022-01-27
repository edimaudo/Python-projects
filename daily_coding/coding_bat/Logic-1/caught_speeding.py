#You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    if speed <= 60 and is_birthday==False:
        return 0
    elif (speed >= 61 and speed <=80) and is_birthday==False:
        return 1
    elif speed >= 81 and is_birthday==False:
        return 2
    else:
        if (speed >= 66 and speed <=85) and is_birthday==True:
            return 1
        elif speed >= 86 and is_birthday==True:
            return 2
        else:
            return 0
        

print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))
print(caught_speeding(85, True))
print(caught_speeding(75, True))
print()
