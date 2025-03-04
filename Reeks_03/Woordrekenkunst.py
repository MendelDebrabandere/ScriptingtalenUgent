def alfabet(puzzel):
    """
    >>> alfabet('BEAR + RARE + ERE = RHYME')
    'ABEHMRY'
    >>> alfabet('BRUTUS + STABS = CAESAR')
    'ABCERSTU'
    """

    alph = sorted(c for c in puzzel if c.isalpha())
    unique_alph = []
    for c in alph:
        if c not in unique_alph:
            unique_alph.append(c)

    return ''.join(unique_alph)


def getal(w, alph, opl):
    """
    >>> getal('BEAR', 'ABEHMRY', '5790813')
    7951
    >>> getal('RARE', 'ABEHMRY', '5790813')
    1519
    >>> getal('ERE', 'ABEHMRY', '5790813')
    919
    >>> getal('RHYME', 'ABEHMRY', '5790813')
    10389
    """

    num = ''
    for c in w:
        num += opl[alph.find(c)]

    return int(num)


def getallen(s, alph, opl):
    """
    >>> getallen('BEAR + RARE + ERE', 'ABEHMRY', '5790813')
    (7951, 1519, 919)
    >>> getallen('BRUTUS + STABS', 'ABCERSTU', '75638921')
    (581219, 92759)
    """

    return tuple(getal(w, alph, opl) for w in s.split(' + '))


def woord(g, alph, opl):
    """
    >>> woord(7951, 'ABEHMRY', '5790813')
    'BEAR'
    >>> woord(1519, 'ABEHMRY', '5790813')
    'RARE'
    >>> woord(919, 'ABEHMRY', '5790813')
    'ERE'
    >>> woord(10389, 'ABEHMRY', '5790813')
    'RHYME'
    """

    w = ''
    for c in str(g):
        w += alph[opl.find(c)]

    return w


def uitkomst(som, alph, opl):
    """
    >>> uitkomst('BEAR + RARE + ERE', 'ABEHMRY', '5790813')
    'RHYME'
    >>> uitkomst('BRUTUS + STABS', 'ABCERSTU', '75638921')
    'CAESAR'
    """

    return woord(sum(getallen(som, alph, opl)), alph, opl)


def isoplossing(s, opgave):
    """
    >>> isoplossing('5790813', 'BEAR + RARE + ERE = RHYME')
    True
    >>> isoplossing('75638921', 'BRUTUS + STABS = TIBERIUS')
    False
    >>> isoplossing('06824', 'BLACK + SILK = JACKET')
    False
    >>> isoplossing('6668863325', 'COSA + NOSTRA = CRIMES')
    False
    """

    # elk cijfer in de opl moet uniek zijn
    for c in s:
        if s.count(c) != 1:
            return False


    alph = alfabet(opgave)

    # de lengte van het alphabet en de oplosing moet hetzelfde zijn
    if len(alph) != len(s):
        return False

    LL, RL = opgave.split(' = ')
    return sum(getallen(LL, alph, s)) == getal(RL, alph, s)

















if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
