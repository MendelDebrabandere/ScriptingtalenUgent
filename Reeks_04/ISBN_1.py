def isISBN(c, isbn13=True):
    """
    >>> isISBN('9789027439642', False)
    False
    >>> isISBN('9789027439642', True)
    True
    >>> isISBN('9789027439642')
    True
    >>> isISBN('080442957X')
    False
    >>> isISBN('080442957X', False)
    True
    """

    if not isinstance(c, str):
        return False
    if isbn13 and len(c) != 13:
        return False
    if not isbn13 and len(c) != 10:
        return False


    if not isbn13:
        checksum = sum( (i+1) * int(c[i]) for i in range(9) ) % 11
        checkval = 10 if c[-1] == 'X' else int(c[-1])
        return checkval == checksum
    elif isbn13:
        o = sum(int(i) for i in c[0:-1:2])
        e = sum(int(i) for i in c[1:-1:2])
        return int(c[-1]) == 10 - (o+3*e) % 10


    return False



def zijnISBN(codes, isbn13=None):
    """
    >>> codes = ['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146']
    >>> zijnISBN(codes)
    [False, True, True, True, False, False, False, True, False]
    >>> zijnISBN(codes, True)
    [False, False, False, False, False, False, False, True, False]
    >>> zijnISBN(codes, False)
    [False, True, True, True, False, False, False, False, False]
    >>> codes04 = ['0123456780', '0123456781', '0123456782', '0123456783', '0123456784', '0123456785', '0123456786', '0123456787', '0123456788', '0123456789']
    >>> zijnISBN(codes04)
    [False, False, False, False, False, False, False, False, False, True]
    """

    isbns = []
    for code in codes:
        if isinstance(code, str):
            if isbn13 is not None:
                isbns.append(isISBN(code, isbn13))
            else:
                isbns.append(isISBN(code, len(code) == 13))
        else:
            isbns.append(False)

    return isbns












if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)