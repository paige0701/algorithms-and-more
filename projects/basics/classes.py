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

        common = self.gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    @staticmethod
    def gcd(m, n):
        while m % n != 0:
            m, n = n, m % n
        return n


if __name__ == '__main__':
    fraction = Fraction(3, 5)
    fraction2 = Fraction(1, 5)
    print((Fraction(1, 4) + Fraction(1, 2)))