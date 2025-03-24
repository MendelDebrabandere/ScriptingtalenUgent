
class ISBN13:
    """
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isvalid()
    True
    >>> code.asISBN10()
    '0-13611067-3'
    """

    def __init__(self, code, spec_len=1):
        self.code = str(code)
        self.spec_len = spec_len
        assert 1 <= spec_len <= 5, 'invalid ISBN code'

    def __str__(self):
        return self.code[:3] + '-' + self.code[3:3+self.spec_len] + '-' + self.code[3+self.spec_len:12] + '-' + self.code[12]

    def __repr__(self):
        return 'ISBN13(' + self.code + ', ' + str(self.spec_len) + ')'

    def isvalid(self):
        if len(self.code) != 13 or self.code[:3] not in {'978', '979'}:
            return False

        o = sum(int(i) for i in self.code[:-1:2])
        e = sum(int(i) for i in self.code[1:-1:2])

        return int(self.code[-1]) == (10 - (o + 3 * e) % 10) % 10

    def asISBN10(self):
        if self.code[0:3] != '978' or not self.isvalid():
            return None

        check_num = sum((i+1) * int(self.code[i+3]) for i in range(9)) % 11

        if check_num == 10:
            check_num = 'X'

        return str(self)[4:-1] + str(check_num)


if __name__ == '__main__':
    import doctest
    doctest.testmod()