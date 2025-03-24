def rooster(n, wijzers):
    """
    >>> vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    >>> vierkant
    [['>', '>', '>', '>'], ['^', '<', '^', 'v'], ['^', 'v', '^', '^'], ['>', '>', 'v', '>']]
    >>> rooster(4, '>>>>^<^v^v^>>v>')
    Traceback (most recent call last):
    AssertionError: ongeldige argumenten
    """

    assert len(wijzers) == n * n, "ongeldige argumenten"

    returnlijst = []
    for i in range(n):
        internallijst = []
        for j in range(n):
            internallijst.append(wijzers[i*n + j])
        returnlijst.append(internallijst)

    return returnlijst


def tekst(r):
    """
    >>> vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    >>> vierkant
    [['>', '>', '>', '>'], ['^', '<', '^', 'v'], ['^', 'v', '^', '^'], ['>', '>', 'v', '>']]
    >>> print(tekst(vierkant))
    > > > >
    ^ < ^ v
    ^ v ^ ^
    > > v >
    """

    return '\n'.join(' '.join(l) for l in r)


def stap(r, pos):
    """
    >>> vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    >>> vierkant
    [['>', '>', '>', '>'], ['^', '<', '^', 'v'], ['^', 'v', '^', '^'], ['>', '>', 'v', '>']]
    >>> print(tekst(vierkant))
    > > > >
    ^ < ^ v
    ^ v ^ ^
    > > v >
    >>> stap(vierkant, (3, 0))
    (3, 1)
    >>> print(tekst(vierkant))
    > > > >
    ^ < ^ v
    ^ v ^ ^
    v > v >
    >>> stap(vierkant, (3, 1))
    (3, 2)
    >>> print(tekst(vierkant))
    > > > >
    ^ < ^ v
    ^ v ^ ^
    v v v >
    """

    directions = ['^', '>', 'v', '<']
    directionsMeaning = [(-1, 0), (0, 1), (1, 0), (0,-1)]

    currChar = r[pos[0]][pos[1]]
    dirIndex = directions.index(currChar)
    dirTuple = directionsMeaning[dirIndex]
    r[pos[0]][pos[1]] = directions[(dirIndex + 1) % 4]

    return clampToPosField(tupleSom(pos, dirTuple), len(r))

def tupleSom(t1, t2):
    return tuple(a + b for a, b in zip(t1,t2))

def clampToPosField(pos, l):
    return clampNumToField(pos[0], l), clampNumToField(pos[1], l)

def clampNumToField(num, length):
    if num < 0:
        return 0
    elif num >= length:
        return length-1
    return num

def stappen(r):
    """
    >>> vierkant = rooster(4, '>>>>^<^v^v^^>>v>')
    >>> print(tekst(vierkant))
    > > > >
    ^ < ^ v
    ^ v ^ ^
    > > v >
    >>> stappen(vierkant)
    [(3, 0), (3, 1), (3, 2), (3, 2), (3, 1), (3, 1), (3, 0), (3, 0), (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3)]
    >>> print(tekst(vierkant))
    v v v >
    > < ^ v
    > v ^ ^
    > ^ ^ >
    """

    mierLoc = (len(r)-1, 0)
    steps = [mierLoc]

    while mierLoc != (0, len(r)-1):
        mierLoc = clampToPosField(stap(r, mierLoc), len(r))
        steps.append(mierLoc)

    return steps























if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)