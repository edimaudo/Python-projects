import math
import random
from collections import Counter
import operator

def generate_random(alist):
    return random.randint(0,len(alist)-1)

def move(currentPosition,allPosition):
    tempval = allPosition[currentPosition]
    return tempval[generate_random(tempval)]

def main():
    city = ["Chicago","New York City","Portland","Palo Alto","India","Germany","Russia","Atlanta"]
    
    countries = {
    "Chicago":["New York City","Portland","Palo Alto"],
    "New York City":["Chicago","Portland","India"],
    "Portland":["Chicago","New York City","Palo Alto","India","Germany"],
    "Palo Alto":["Chicago","Portland"],
    "India":["New York City","Portland","Germany","Russia","Atlanta"],
    "Germany":["India","Portland","Russia"],
    "Russia":["India","Germany","Atlanta"],
    "Atlanta":["India","Russia"]
    }

    currentCountry = []
    startCountry = city[generate_random(city)]
    countval = 0
    maxval = 1000000
    while countval < maxval:
        startCountry = move(startCountry,countries)
        currentCountry.append(startCountry)
        countval+=1
    a = dict(Counter(currentCountry))
    print(a)
    sorted_a = sorted(a.items(), key=operator.itemgetter(1))
    print(sorted_a[len(sorted_a) - 1][0],round(sorted_a[len(sorted_a) - 1][1]/maxval,2))
    
main()