
def sign(num):
    return '-' if num < 0 else '+'

class Quaternion:
    """
    >>> q1 = Quaternion(2, 4, 7, 3)
    >>> q1.norm()
    8.831760866327848
    >>> print(q1)
    2 + 4i + 7j + 3k
    >>> q1
    Quaternion(2, 4, 7, 3)

    >>> q2 = Quaternion(a=-5, c=2, d=-4)
    >>> q2.norm()
    6.708203932499369
    >>> print(q2)
    -5 + 0i + 2j - 4k
    >>> q2
    Quaternion(-5, 0, 2, -4)

    >>> q1 + q2
    Quaternion(-3, 4, 9, -1)
    >>> q2 + q1
    Quaternion(-3, 4, 9, -1)
    >>> q1 + 3
    Quaternion(5, 4, 7, 3)
    >>> 3 + q1
    Quaternion(5, 4, 7, 3)
    >>> q1 * q2
    Quaternion(-12, -54, -15, -15)
    >>> q2 * q1
    Quaternion(-12, 14, -47, -31)
    >>> q1 * 3
    Quaternion(6, 12, 21, 9)
    >>> 3 * q1
    Quaternion(6, 12, 21, 9)
    >>> "Hello World!" + q1
    Traceback (most recent call last):
    AssertionError: Can not add class of type str with a Quaternion
    """




    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    def __str__(self):
        return f'{self.a} {sign(self.b)} {abs(self.b)}i {sign(self.c)} {abs(self.c)}j {sign(self.d)} {abs(self.d)}k'

    def __repr__(self):
        return f'{__class__.__name__}({self.a}, {self.b}, {self.c}, {self.d})'

    def norm(self):
        return (self.a**2 + self.b**2 + self.c**2 + self.d**2)**0.5

    def __add__(self, other):
        if isinstance(other, int):
            return Quaternion(self.a + other, self.b, self.c, self.d)
        if isinstance(other, Quaternion):
            return Quaternion(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
        assert False, f'Can not add class of type {other.__class__.__name__} with a Quaternion'

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, int):
            return Quaternion(self.a * other, self.b * other, self.c * other, self.d * other)
        if isinstance(other, Quaternion):
            a1, b1, c1, d1 = self.a, self.b, self.c, self.d
            a2, b2, c2, d2 = other.a, other.b, other.c, other.d
            a = a1*a2 - b1 * b2 - c1 * c2 - d1 * d2
            b = a1*b2 + b1*a2 + c1*d2 -d1*c2
            c = a1*c2 - b1*d2 + c1*a2 + d1*b2
            d = a1*d2 + b1*c2 - c1*b2 + d1*a2
            return Quaternion(a, b, c, d)
        assert False, f'Can not add class of type {other.__class__.__name__} with a Quaternion'




    def __rmul__(self, other):
        return self * other


























if __name__ == '__main__':
    import doctest
    doctest.testmod()





