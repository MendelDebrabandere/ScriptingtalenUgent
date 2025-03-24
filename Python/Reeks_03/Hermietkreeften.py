def opeenvolgend(reeks):
    """
    >>> opeenvolgend([7, 5, 4, 9, 6, 3, 8])
    True
    >>> opeenvolgend((16, 13, 18, 17, 15, 14, 20))
    False
    >>> opeenvolgend((3, 4, 1, 6, 8, 7))
    False
    """

    reeks = sorted(reeks)
    lastnum = reeks[0]
    for i in range(1, len(reeks)):
        lastnum += 1
        if reeks[i] != lastnum:
            return False
    return True


def goudlokje(reeks):
    """
    >>> goudlokje([7, 5, 4, 9, 6, 3, 8])
    >>> goudlokje((16, 13, 18, 17, 15, 14, 20, 21, 22))
    19
    >>> goudlokje((16, 13, 18, 17, 15, 14, 20))
    19
    >>> goudlokje((3, 4, 1, 6, 8, 7))
    >>> goudlokje((74, 79, 75, 80, 77, 79, 73, 76))
    """

    if opeenvolgend(reeks):
        return None


    reeks = sorted(reeks)
    toegevoegdnum = -1
    lastnum = reeks[0]
    for i in range(1, len(reeks)):
        lastnum += 1
        if reeks[i] != lastnum:
            if toegevoegdnum == -1:
                toegevoegdnum = lastnum
                lastnum += 1
            else:
                return None
    return toegevoegdnum


def verhuizen1(reeks):
    """
    >>> verhuizen1([7, 5, 4, 9, 6, 3, 8])
    [7, 5, 4, 9, 6, 3, 8]
    >>> verhuizen1((16, 13, 18, 17, 15, 14, 20))
    [16, 13, 18, 17, 15, 14, 20, 19]
    >>> verhuizen1((3, 4, 1, 6, 8, 7))
    [3, 4, 1, 6, 8, 7]
    """

    returnlijst = list(reeks)
    addval = goudlokje(reeks)
    if addval:
        returnlijst.append(addval)

    return returnlijst


def verhuizen2(reeks):
    """
    >>> schelpen = [7, 5, 4, 9, 6, 3, 8]
    >>> verhuizen2(schelpen)
    >>> schelpen
    [7, 5, 4, 9, 6, 3, 8]

    >>> schelpen = [16, 13, 18, 17, 15, 14, 20]
    >>> verhuizen2(schelpen)
    >>> schelpen
    [16, 13, 18, 17, 15, 14, 20, 19]

    >>> schelpen = [3, 4, 1, 6, 8, 7]
    >>> verhuizen2(schelpen)
    >>> schelpen
    [3, 4, 1, 6, 8, 7]
    """

    addval = goudlokje(reeks)
    if addval:
        reeks.append(addval)













if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)