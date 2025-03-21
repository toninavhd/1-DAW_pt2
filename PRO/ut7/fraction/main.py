class Fraction:
    
    def __init__(self, num: int, den: int):
        self.gcd_num = self.gcd(num, den)
        self.num = num // self.gcd_num
        self.den = den // self.gcd_num

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __str__(self):
        return f'{self.num}/{self.den}'

    @staticmethod
    def gcd(a: int, b: int) -> int:
        while b > 0:
            a, b = b, a % b
        return a
