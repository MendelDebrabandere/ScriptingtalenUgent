
def rotatie(h, r):
    """
    >>> rotatie('Jessica', 1)
    'essicaJ'
    >>> rotatie('emily', -2)
    'lyemi'
    >>> rotatie('LOUISE', 9)
    'ISELOU'
    """

    r = r % len(h)

    return h[r:] + h[:r]




def rotaties(w):
    """
    >>> rotaties('Jessica') == {'CAJESSI', 'SICAJES', 'JESSICA', 'AJESSIC', 'SSICAJE', 'ESSICAJ', 'ICAJESS'}
    True
    >>> rotaties('emily') == {'YEMIL', 'ILYEM', 'EMILY', 'LYEMI', 'MILYE'}
    True
    >>> rotaties('LOUISE') == {'SELOUI', 'UISELO', 'ELOUIS', 'OUISEL', 'LOUISE', 'ISELOU'}
    True
    """

    rots = set()

    w = w.upper()

    for i, _ in enumerate(w):
        rots.add(rotatie(w,i))

    return rots



def normaalvorm(w):
    """
    >>> normaalvorm('Jessica')
    'AJESSIC'
    >>> normaalvorm('emily')
    'EMILY'
    >>> normaalvorm('LOUISE')
    'ELOUIS'
    """

    return sorted(rotaties(w))[0]


def halskettingen(k, n):
    """
    >>> halskettingen(2, 12)
    352
    >>> halskettingen(3, 7)
    315
    >>> halskettingen(9, 5)
    11817
    >>> halskettingen(21, 4)
    48741
    >>> halskettingen(26, 3)
    5876
    """

    import itertools
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    possibles = set(itertools.product(alphabet[:k], repeat=n))

    uniques = set()

    for p in possibles:
        uniques.add(normaalvorm(''.join(p)))

    return len(uniques)


















if __name__ == "__main__":
    import doctest
    doctest.testmod()