
class Grille:
    """
    >>> grille = Grille(5, [(0, 0), (1, 0), (1, 2), (1, 4), (3, 3), (4, 2)])
    >>> grille.dimension
    5
    >>> grille.apertures == {(1, 2), (0, 0), (3, 3), (1, 4), (4, 2), (1, 0)}
    True
    >>> print(grille)
    O####
    O#O#O
    #####
    ###O#
    ##O##
    >>> grille.decode('message.txt')
    'East, '
    >>> grille.rotate().apertures == {(3, 1), (2, 0), (2, 3), (4, 3), (0, 4), (0, 3)}
    True
    >>> print(grille)
    ###OO
    #####
    O##O#
    #O###
    ###O#
    >>> grille.decode('message.txt')
    'West, '
    >>> grille.rotate().apertures == {(3, 2), (3, 0), (4, 4), (1, 1), (3, 4), (0, 2)}
    True
    >>> print(grille)
    ##O##
    #O###
    #####
    O#O#O
    ####O
    >>> grille.decode('message.txt')
    "home's"
    >>> grille.rotate().apertures == {(0, 1), (1, 3), (2, 1), (4, 1), (2, 4), (4, 0)}
    True
    >>> print(grille)
    #O###
    ###O#
    #O##O
    #####
    OO###
    >>> grille.decode('message.txt')
    ' best.'
    >>> grille.rotate(clockwise=False).apertures == {(3, 2), (3, 0), (4, 4), (1, 1), (3, 4), (0, 2)}
    True
    >>> print(grille)
    ##O##
    #O###
    #####
    O#O#O
    ####O
    >>> grille.decode('message.txt')
    "home's"

    >>> grille1 = Grille(4, ((1, 3), (0, 0), (2, 3), (1, 1)))
    >>> grille2 = Grille(4, {(2, 0), (1, 0), (3, 3), (2, 2)})
    >>> grille3 = Grille(4, [(3, 0), (2, 3), (2, 0), (1, 1)])
    >>> grille4 = Grille(5, ((1, 3), (0, 0), (2, 3), (1, 1)))
    >>> grille1 == grille2
    True
    >>> grille1 == grille3
    False
    >>> grille1 == grille4
    False

    >>> grille5 = grille1 + grille3
    >>> grille5.dimension
    4
    >>> grille5.apertures
    {(2, 3), (1, 1)}
    >>> print(grille5)
    ####
    #O##
    ###O
    ####
    >>> grille1 + grille4
    Traceback (most recent call last):
    AssertionError: invalid operation
    """

    def __init__(self, n, apertures):
        self.dimension = n
        self.apertures = set(apertures)

    def decode(self, filename):
        code = ''
        with open(filename, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for pos in sorted(self.apertures):
                code += data[pos[0]][pos[1]]
        return code

    def __str__(self):
        str = ''
        for i in range(self.dimension):
            for j in range(self.dimension):
                if (i,j) in self.apertures:
                    str += 'O'
                else:
                    str += '#'
            str += '\n'
        str = str[:-1]
        return str

    def rotate(self, clockwise=True):
        new_apertures = set()
        for aperture in self.apertures:
            if clockwise:
                new_apertures.add( (aperture[1], self.dimension - aperture[0] - 1) )
            else:
                new_apertures.add( (self.dimension - aperture[1] - 1, aperture[0]) )

        self.apertures = new_apertures
        return self

    def  __eq__(self, other):
        if self.dimension != other.dimension:
            return False

        isEverSame = False
        for _ in range(4):
            self.rotate()
            if self.apertures == other.apertures:
                isEverSame = True # not allowed to return here, since we need to rotate back to our beginning

        return isEverSame

    def __add__(self, other):
        assert self.dimension == other.dimension, 'invalid operation'

        new_apertures = set()
        for aperture in self.apertures:
            if aperture in other.apertures:
                new_apertures.add(aperture)

        return Grille(self.dimension, new_apertures)






























if __name__ == '__main__':
    import doctest
    doctest.testmod()










