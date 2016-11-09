def gcd(m,n):
    while n:
        m, n = n, m%n
    return m

class Fraction:
    #constructor
    def __init__(self, top, bottom):
        self.num = top
        self.denom = bottom
        if not isinstance(self.num,int) or not isinstance(self.denom,int):
            self.num = int(self.num)
            self.denom = int(self.denom)
        common = gcd(self.num,self.denom)
        self.num = self.num//common
        self.denom = self.denom//common           
  

    def __str__(self):
        return str(self.num)+"/"+str(self.denom)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.denom + self.denom*otherfraction.num
        newdenom = self.denom*otherfraction.denom
        return Fraction(newnum,newdenom)

    def __eq__(self, otherfraction):
        firstnum = self.num * otherfraction.denom
        secondnum = self.denom * otherfraction.num
        return firstnum == secondnum

    def __sub__(self,otherfraction):
        firstnum = self.num * otherfraction.denom - self.denom * otherfraction.num
        secondnum = self.denom * otherfraction.denom
        common = gcd(firstnum,secondnum)
        return Fraction(firstnum//common,int(secondnum/common))

    def __mul__(self,otherfraction):
        firstnum = self.num * otherfraction.num
        secondnum = self.denom * otherfraction.denom
        common = gcd(firstnum,secondnum)
        return Fraction(firstnum//common,secondnum//common)

    def __truediv__(self,otherfraction):
        firstnum = self.num * otherfraction.denom
        secondnum = self.denom * otherfraction.num
        common = gcd(firstnum, secondnum)
        return Fraction(int(firstnum//common),int(secondnum//common))

    def __ne__(self,otherfraction):
        firstnum = self.num * otherfraction.denom
        secondnum = self.denom * otherfraction.num
        return firstnum != secondnum

    def __gt__(self,otherfraction):
        firstnum = self.num * otherfraction.denom
        secondnum = self.denom * otherfraction.nom
        return firstnum > secondnum

    def __ge__(self,otherfraction):
        firstnum = self.num * otherfraction.denom
        secondnum = self.denom * otherfraction.num
        return firstnum >= secondnum

    def __lt__(self,otherfraction):
        firstnum = self.num * otherfraction.denom
        secondnum = self.denom * otherfraction.num
        return firstnum < secondnum

    def __le__(self,otherfraction):
        firstnum = self.num * otherfraction.denom
        secondnum = self.denom * otherfraction.num
        return firstnum <= secondnum


    def getNum(self):
        return self.num

    def getDen(self):
        return self.denom



def main():
    f1 = Fraction(1,2)
    f2 = Fraction(3,6)
    f3 = Fraction(1,3)
    print(f1.getNum())
    #print(f1+f2)
    #print(f2)
    #print(f3)


main()
