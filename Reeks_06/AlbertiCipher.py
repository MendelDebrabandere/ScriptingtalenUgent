
class Formula:
    """
    >>> wheel = Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> wheel
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  abcdefghijklmnopqrstuvwxyz
    >>> wheel.encode_symbol('K')
    'k'
    >>> wheel.decode_symbol('x')
    'X'
    >>> wheel.rotate(2)
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'cdefghijklmnopqrstuvwxyzab')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  cdefghijklmnopqrstuvwxyzab
    >>> wheel.encode_symbol('K')
    'm'
    >>> wheel.decode_symbol('x')
    'V'
    >>> wheel.rotate(11)
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'nopqrstuvwxyzabcdefghijklm')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  nopqrstuvwxyzabcdefghijklm
    >>> wheel.rotate(-5)
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ijklmnopqrstuvwxyzabcdefgh')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  ijklmnopqrstuvwxyzabcdefgh
    >>> wheel.reset()
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> print(wheel)
    stabilis: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    mobilis:  abcdefghijklmnopqrstuvwxyz
    >>> wheel.encode('DECIFRIS', 1, 2, 3)
    'efdliunx'
    >>> wheel.decode('efdliunx', 1, 2, 3)
    'DECIFRIS'

    >>> Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') + 3
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabc')
    >>> 3 + Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabc')
    >>> Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz') - 3
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'xyzabcdefghijklmnopqrstuvw')
    >>> 3 - Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'xyzabcdefghijklmnopqrstuvw')
    >>> wheel = Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz')
    >>> wheel += 3
    >>> wheel
    Formula('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'defghijklmnopqrstuvwxyzabc')
    """

    def __init__(self, stabilis, mobilis):
        self.stabilis = str(stabilis)
        self.mobilis = str(mobilis)
        self.rot = 0

        assert len(stabilis) == len(mobilis), 'invalid wheel'

        for c in stabilis:
            assert stabilis.count(c) == 1, 'invalid wheel'
        for c in mobilis:
            assert mobilis.count(c) == 1, 'invalid wheel'

    def __repr__(self):
        return f"{__class__.__name__}('{self.stabilis}', '{self.mobilis}')"

    def __str__(self):
        return f"stabilis: {self.stabilis}\nmobilis:  {self.mobilis}"

    def reset(self):
        self.rotate(-self.rot)
        return self

    def rotate(self, r):
        assert isinstance(r, int), 'invalid rotation'

        if r == 0:
            return self

        newMobilis = ''
        for idx in range(r, r + len(self.mobilis)):
            newMobilis += self.mobilis[idx % len(self.mobilis)]

        self.mobilis = newMobilis
        self.rot += r
        return self

    def encode_symbol(self, s):
        assert s in self.stabilis, 'invalid symbol'
        return self.mobilis[self.stabilis.find(s)]

    def decode_symbol(self, s):
        assert s in self.mobilis, 'invalid symbol'
        return self.stabilis[self.mobilis.find(s)]

    def encode(self, t, ri, rp, p, enc=True):
        totalRot = ri
        self.rotate(ri)
        word = ''
        counter = 0
        for c in t:
            word += self.encode_symbol(c) if enc else self.decode_symbol(c)
            counter += 1
            if counter >= p:
                counter = 0
                self.rotate(rp)
                totalRot += rp

        self.rotate(-totalRot)
        return word

    def decode(self, t, ri, rp, p):
        return self.encode(t, ri, rp, p, False)

    def __add__(self, other):
        assert isinstance(other, int), 'invalid rotation'
        form = Formula(self.stabilis, self.mobilis)
        return form.rotate(other)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        assert isinstance(other, int), 'invalid rotation'
        form = Formula(self.stabilis, self.mobilis)
        return form.rotate(-other)

    def __rsub__(self, other):
        return self - other




if __name__ == '__main__':
    import doctest
    doctest.testmod()