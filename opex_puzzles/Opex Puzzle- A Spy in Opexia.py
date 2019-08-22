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
    countries = {
    "Ecuador":["Columbia","Peru","Brazil"],
    "Columbia":["Ecuador","Peru","Venezuela","Brazil"],
    "Venezuela":["Columbia","Guyana","Brazil"],
    "Guyana":["Venezuela","Suriname","Brazil"],
    "Suriname":["Guyana","French Guiana","Brazil"],
    "French Guiana":["Suriname","Brazil"],
    "Brazil":["Guyana","French Guiana","Suriname","Venezuela","Columbia","Peru","Bolivia","Paraguay","Argentina","Uruguay"],
    "Uruguay":["Argentina","Brazil"],
    "Paraguay":["Bolivia","Argentina","Brazil"],
    "Bolivia":["Brazil","Peru","Chile","Argentina","Paraguay"],
    "Peru":["Ecuador","Brazil","Bolivia","Columbia","Chile"],
    "Chile":["Peru","Bolivia","Argentina"],
    "Argentina":["Chile","Bolivia","Paraguay","Brazil","Uruguay"]
    }

    currentCountry = []
    startCountry = "Chile"
    countval = 0
    maxval = 1000
    while countval < maxval:
        startCountry = move(startCountry,countries)
        currentCountry.append(startCountry)
        countval+=1
    a = dict(Counter(currentCountry))
    print(a)
    sorted_a = sorted(a.items(), key=operator.itemgetter(1))
    print(sorted_a[len(sorted_a) - 1][0],round(sorted_a[len(sorted_a) - 1][1]/maxval,2))
    
main()