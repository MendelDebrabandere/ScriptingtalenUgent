def cijferfrequentie(s):
    """
    >>> cijferfrequentie('10 71 32 23 14 15 16 27 18 19')
    (1, 7, 3, 2, 1, 1, 1, 2, 1, 1)
    >>> cijferfrequentie('F1gur471v3ly 5p34k1ng?')
    (0, 3, 0, 2, 2, 1, 0, 1, 0, 0)
    """

    cijfers = [int(c) for c in s if c.isdigit()]
    ret = []
    for i in range(10):
        ret.append(cijfers.count(i))

    return tuple(ret)

def beschrijving(b):
    """
    >>> beschrijving((1, 7, 3, 2, 1, 1, 1, 2, 1, 1))
    '10 71 32 23 14 15 16 27 18 19'
    >>> beschrijving((0, 3, 0, 2, 2, 1, 0, 1, 0, 0))
    '0 31 2 23 24 15 6 17 8 9'
    """
    l = [f'{c}{i}' if c != 0 else str(i) for i, c in enumerate(b,0)]
    return " ".join(l)


def iszelfbeschrijvend(reeks):
    """
    >>> iszelfbeschrijvend(['10 71 32 23 14 15 16 27 18 19'])
    True
    >>> iszelfbeschrijvend(['F1gur471v3ly 5p34k1ng?'])
    False
    >>> iszelfbeschrijvend([
    ...     '10 71 32 23 14 15 16 27 18 19',
    ...     '20 81 72 53 44 35 26 47 38 29'
    ... ])
    True
    >>> iszelfbeschrijvend((
    ...     '10 71 32 23 14 15 16 27 18 19',
    ...     '20 81 72 53 44 35 26 47 38 29',
    ...     '40 101 82 73 64 65 56 77 58 39',
    ...     '60 131 92 93 74 75 86 107 88 69',
    ...     '80 201 122 113 84 85 96 117 138 89'
    ... ))
    True
    """
    expectedreeks = [0 for i in range(10)]
    for i, r in enumerate(reeks):
        for k in range(10):
            expectedreeks[k] += r.count(str(k))
        if beschrijving(expectedreeks) != r:
            return False


    return True



def iszelfbeschrijvend_2(*args):
    """
    >>> iszelfbeschrijvend_2('10 71 32 23 14 15 16 27 18 19')
    True
    >>> iszelfbeschrijvend_2('F1gur471v3ly 5p34k1ng?')
    False
    >>> iszelfbeschrijvend_2(
    ...     '10 71 32 23 14 15 16 27 18 19',
    ...     '20 81 72 53 44 35 26 47 38 29'
    ... )
    True
    >>> iszelfbeschrijvend_2(
    ...     '10 71 32 23 14 15 16 27 18 19',
    ...     '20 81 72 53 44 35 26 47 38 29',
    ...     '40 101 82 73 64 65 56 77 58 39',
    ...     '60 131 92 93 74 75 86 107 88 69',
    ...     '80 201 122 113 84 85 96 117 138 89'
    ... )
    True
    """

    return iszelfbeschrijvend(args)














if __name__ == "__main__":
    import doctest
    doctest.testmod()
