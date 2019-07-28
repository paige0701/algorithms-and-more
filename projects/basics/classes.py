class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

if __name__ == '__main__':
    fraction = Fraction(3,5)
    fraction2 = Fraction(1,5)
    print(fraction + fraction2
          )