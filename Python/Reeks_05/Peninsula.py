def touchesS(rij, kolom, data):
    if rij-1 >= 0 and data[rij-1][kolom] == 'S':
        return True
    if rij+1 < len(data) and data[rij+1][kolom] == 'S':
        return True
    if kolom-1 >= 0 and data[rij][kolom-1] == 'S':
        return True
    if kolom+1 < len(data[0]) and data[rij][kolom+1] == 'S':
        return True

    return False


def landmass(filename):
    """
    >>> landmass('landmass1.txt')
    (0, 196)
    >>> landmass('landmass2.txt')
    (6, 169)
    >>> landmass('landmass3.txt')
    (8, 45)
    """

    o = 0
    r = 0

    with open(filename, 'r') as invoer:
        data = invoer.readlines()

    for rij, lijn in enumerate(data):
        for kolom, char in enumerate(lijn):
            if char == 'S':
                o += 1
            if char == '#' and touchesS(rij, kolom, data):
                r += 1

    return r, o


def landtype(filename, ratio=0.05):
    """
    >>> landtype('landmass1.txt')
    'island'
    >>> landtype('landmass2.txt')
    'peninsula'
    >>> landtype('landmass3.txt')
    'mainland'
    >>> landtype('landmass3.txt', ratio=0.2)
    'peninsula'
    """

    mass = landmass(filename)

    if mass[0] == 0:
        return 'island'

    if mass[0]/mass[1] > ratio:
        return 'mainland'

    return 'peninsula'










if __name__ == '__main__':
    import doctest
    doctest.testmod()