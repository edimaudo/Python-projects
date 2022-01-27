#The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

def squirrel_play(temp, is_summer):
    if (temp >= 60 and temp <=90) and is_summer==False:
        return True
    elif (temp >= 60 and temp <=100) and is_summer==True:
        return True
    return False



print(squirrel_play(70, False)) 
print(squirrel_play(95, False))
print(squirrel_play(95, True))
