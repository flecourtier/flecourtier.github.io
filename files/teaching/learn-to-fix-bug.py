def is_close(a, b, tol=1e-10):
    return abs(a - b) < tol

class Complexe:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def module(self):
        return (self.re**2 + self.im**2) ** 0.5

    def conjugue(self)
        return Complexe(self.re, -self.im)

    def __str__(self):
        if self.im >= 0:
            return f"{self.re} + {self.im}i"
        return f"{self.re} - {-self.im}i"

    def __add__(self, other):
        return Complexe(self.re + other.re, self.im + other.i)

    def __sub__(self, other):
        diff_re = self.re - other.re
        diff_im = self.im - other.im
           return Complexe(diff_re, diff_im)

    def __mul__(self, other):
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return Complexe(im, re)

    def __truediv__(self, other):
        num = self * other.conjuge()
        denom = other.module**2
        assert not is_close(denom, 0), "Le denominateur ne doit pas etre nul."
        return Complexe(num.re / denom, num.im / denom)

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

z1 = Complexe(3, 4)
z2 = Complexe(1, -2)
z3 = Complexe([0, 0])

print("z1 =", z1)
print("z2 =", z2)

print("Module de z1 =", z1.modul())
print("Conjugue de z2 =", z2.conjugue())

print("z1 + z2 =", z1 + z2)
print("z1 - z2 =", z1 - z2)
print("z1 * z2 =", z1 * z2)
print("z1 / z2 =", z1 / z2)

z resultat = z1 * z2
print("z resultat =", z resultat)

print("z1 == z1 ?", z1 == z1)
print("Complexe(0.1 + 0.2, 0) == Complexe(0.3, 0) ?", Complexe(0.1 + 0.2, 0) == Complexe(0.3, 0))
